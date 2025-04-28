from agents.pragmatic_pete import PragmaticPete
from agents.innovative_izzy import InnovativeIzzy
from agents.risk_averse_riley import RiskAverseRiley
from agents.scalable_sam import ScalableSam
from agents.senior_dev_sam import SeniorDevSam
from typing import List, Dict, Any, Optional
import yaml
import os

class BattleConfig:
    def __init__(self, config_file: Optional[str] = None):
        self.default_config = {
            "voting_weights": {
                "recommendations": 1.0,
                "benefits": 0.5,
                "risks": -0.3,
                "implementation": 0.7
            },
            "agents": {
                "Pragmatic Pete": {
                    "focus_areas": ["Business value", "ROI", "Market analysis", "Cost-benefit analysis"],
                    "biases": ["Favors proven solutions", "Prioritizes immediate business value"],
                    "voting_style": "generous"  # generous, moderate, conservative
                },
                "Innovative Izzy": {
                    "focus_areas": ["Cutting-edge technology", "User experience", "Future-proofing"],
                    "biases": ["Favors modern solutions", "Prioritizes user experience"],
                    "voting_style": "moderate"
                },
                "Risk-Averse Riley": {
                    "focus_areas": ["Security", "Reliability", "Compliance", "Risk mitigation"],
                    "biases": ["Favors proven security patterns", "Prioritizes stability"],
                    "voting_style": "conservative"
                },
                "Scalable Sam": {
                    "focus_areas": ["System architecture", "Performance", "Resource optimization"],
                    "biases": ["Favors scalable solutions", "Prioritizes performance"],
                    "voting_style": "moderate"
                },
                "Senior Dev Sam": {
                    "focus_areas": ["Code quality", "Technical debt", "Best practices"],
                    "biases": ["Favors maintainable code", "Prioritizes best practices"],
                    "voting_style": "conservative"
                }
            }
        }
        
        self.config = self.default_config.copy()
        if config_file and os.path.exists(config_file):
            with open(config_file, 'r') as f:
                user_config = yaml.safe_load(f)
                self._merge_configs(user_config)
    
    def _merge_configs(self, user_config: Dict[str, Any]) -> None:
        """Merge user configuration with defaults"""
        if "voting_weights" in user_config:
            self.config["voting_weights"].update(user_config["voting_weights"])
        
        if "agents" in user_config:
            for agent_name, agent_config in user_config["agents"].items():
                if agent_name in self.config["agents"]:
                    self.config["agents"][agent_name].update(agent_config)
    
    def get_agent_config(self, agent_name: str) -> Dict[str, Any]:
        """Get configuration for a specific agent"""
        return self.config["agents"].get(agent_name, {})
    
    def get_voting_weights(self) -> Dict[str, float]:
        """Get the voting weights configuration"""
        return self.config["voting_weights"]

def format_list(items: List[str], indent: int = 4) -> str:
    """Format a list of items with proper indentation"""
    if not items:
        return "None"
    return "\n".join(" " * indent + "- " + item for item in items)

def calculate_solution_score(agent_suggestions: List[str], other_solution: Dict[str, Any], 
                           weights: Dict[str, float], voting_style: str) -> float:
    """Calculate how well a solution aligns with an agent's suggestions"""
    score = 0.0
    if not other_solution:
        return score
        
    # Convert suggestions and solution elements to lowercase for comparison
    agent_suggestions_lower = [s.lower() for s in agent_suggestions]
    
    # Apply voting style multiplier
    style_multiplier = {
        "generous": 1.2,
        "moderate": 1.0,
        "conservative": 0.8
    }.get(voting_style, 1.0)
    
    # Check recommendations alignment
    recommendations = []
    if isinstance(other_solution.get('recommendations'), list):
        recommendations = [r.lower() for r in other_solution['recommendations']]
    elif isinstance(other_solution.get('recommendations'), dict):
        recommendations = [str(v).lower() for v in other_solution['recommendations'].values()]
    
    for suggestion in agent_suggestions_lower:
        for rec in recommendations:
            if any(keyword in rec for keyword in suggestion.split()):
                score += weights["recommendations"] * style_multiplier
                break
    
    # Check benefits alignment
    benefits = []
    if isinstance(other_solution.get('benefits'), list):
        benefits = [b.lower() for b in other_solution['benefits']]
    elif isinstance(other_solution.get('benefits'), dict):
        benefits = [str(v).lower() for v in other_solution['benefits'].values()]
    
    for suggestion in agent_suggestions_lower:
        for benefit in benefits:
            if any(keyword in benefit for keyword in suggestion.split()):
                score += weights["benefits"] * style_multiplier
                break
    
    # Check risks alignment
    risks = []
    if isinstance(other_solution.get('risks'), list):
        risks = [r.lower() for r in other_solution['risks']]
    elif isinstance(other_solution.get('risks'), dict):
        risks = [str(v).lower() for v in other_solution['risks'].values()]
    
    for suggestion in agent_suggestions_lower:
        for risk in risks:
            if any(keyword in risk for keyword in suggestion.split()):
                score += weights["risks"] * style_multiplier
                break
    
    # Check implementation alignment
    implementation = other_solution.get('implementation', {})
    if isinstance(implementation, dict):
        complexity = str(implementation.get('complexity', '')).lower()
        time_to_market = str(implementation.get('time_to_market', '')).lower()
        if 'simple' in complexity or 'fast' in time_to_market:
            score += weights["implementation"] * style_multiplier
    
    return score

def run_battle(problem: str, config: Optional[BattleConfig] = None) -> None:
    """Run a battle between all agents"""
    if config is None:
        config = BattleConfig()
    
    # Initialize agents with configuration
    agents = [
        PragmaticPete("Pragmatic Pete", config.get_agent_config("Pragmatic Pete")),
        InnovativeIzzy("Innovative Izzy", config.get_agent_config("Innovative Izzy")),
        RiskAverseRiley("Risk-Averse Riley", config.get_agent_config("Risk-Averse Riley")),
        ScalableSam("Scalable Sam", config.get_agent_config("Scalable Sam")),
        SeniorDevSam("Senior Dev Sam", config.get_agent_config("Senior Dev Sam"))
    ]
    
    # Get voting weights
    weights = config.get_voting_weights()
    
    # Collect initial analyses
    analyses: Dict[str, Dict[str, List[str]]] = {}
    print("\n=== Initial Analyses ===")
    for agent in agents:
        # Use generate_analysis instead of analyze_problem directly
        analysis = agent.generate_analysis(problem)
        analyses[agent.name] = {
            "pros": analysis.get("pros", []),
            "cons": analysis.get("cons", []),
            "risks": analysis.get("risks", []),
            "suggestions": analysis.get("suggestions", []),
            "summary": analysis.get("summary", [])
        }
        print(f"\n{agent.name}'s Analysis:")
        print("Pros:")
        print(format_list(analysis['pros']))
        print("Cons:")
        print(format_list(analysis['cons']))
        print("Risks:")
        print(format_list(analysis['risks']))
        print("Suggestions:")
        print(format_list(analysis['suggestions']))
        if "summary" in analysis:
            print("\nSummary:")
            print(format_list(analysis['summary']))
    
    # Generate rebuttals
    print("\n=== Rebuttals ===")
    rebuttals: Dict[str, Dict[str, str]] = {}
    for agent in agents:
        rebuttals[agent.name] = {}
        other_agents = [a for a in agents if a != agent]
        for other_agent in other_agents:
            # Pass only the specific agent's analysis
            rebuttal = agent.generate_rebuttal(analyses[other_agent.name])
            if rebuttal.strip():  # Only show non-empty rebuttals
                rebuttals[agent.name][other_agent.name] = rebuttal
                print(f"\n{agent.name} responds to {other_agent.name}:")
                print(rebuttal)
    
    # Generate solutions and collect votes
    print("\n=== Solutions and Voting ===")
    solutions: Dict[str, Dict[str, Any]] = {}
    votes: Dict[str, float] = {agent.name: 0.0 for agent in agents}
    
    # First, generate all solutions
    for agent in agents:
        context = {
            "technical_analysis": agent.analyze_problem(problem),
            "other_analyses": {name: analysis for name, analysis in analyses.items() if name != agent.name},
            "rebuttals": rebuttals.get(agent.name, {}),
            "persona": agent.persona
        }
        solution = agent.generate_solution(problem, context)
        solutions[agent.name] = {
            "recommendations": solution.get("recommendations", []),
            "benefits": solution.get("benefits", []),
            "risks": solution.get("risks", []),
            "implementation": solution.get("implementation", {})
        }
        print(f"\n{agent.name}'s Solution:")
        print("Recommendations:")
        print(format_list(solution.get('recommendations', [])))
    
    # Then, have each agent vote based on alignment with their suggestions
    print("\nVoting Process:")
    for voter in agents:
        voter_suggestions = analyses[voter.name]['suggestions']
        voter_config = config.get_agent_config(voter.name)
        voting_style = voter_config.get('voting_style', 'moderate')
        
        for candidate in agents:
            if voter != candidate:
                score = calculate_solution_score(
                    voter_suggestions, 
                    solutions[candidate.name],
                    weights,
                    voting_style
                )
                votes[candidate.name] += score
                if score > 0:
                    print(f"{voter.name} gives {score:.1f} points to {candidate.name}")
    
    # Print results
    print("\n=== Final Results ===")
    print("\nVoting Results:")
    # Sort by vote count
    sorted_votes = sorted(votes.items(), key=lambda x: x[1], reverse=True)
    for agent_name, vote_count in sorted_votes:
        print(f"{agent_name}: {vote_count:.1f} points")
    
    # Determine winner(s)
    max_votes = max(votes.values())
    winners = [name for name, vote_count in votes.items() if abs(vote_count - max_votes) < 0.1]
    
    if len(winners) == 1:
        print(f"\nWinner: {winners[0]}")
        winning_solution = solutions[winners[0]]
        print("\nWinning Recommendations:")
        print(format_list(winning_solution.get('recommendations', [])))
    else:
        print(f"\nTie between: {', '.join(winners)}")
        print("\nShared Recommendations:")
        shared_recs = set()
        for winner in winners:
            recs = set(solutions[winner].get('recommendations', []))
            if not shared_recs:
                shared_recs = recs
            else:
                shared_recs &= recs
        print(format_list(list(shared_recs)))

if __name__ == "__main__":
    print("Welcome to the AI Arena!")
    print("This battle system will analyze your product idea or feature using multiple AI agents.")
    print("Each agent will provide their unique perspective and vote on the best approach.")
    
    # Check for configuration file
    config_file = "battle_config.yaml"
    config = BattleConfig(config_file) if os.path.exists(config_file) else None
    
    problem = input("\nEnter a product idea or feature to analyze: ")
    try:
        run_battle(problem, config)
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        print("Please make sure all agent classes are properly implemented and try again.") 