from typing import List, Dict, Any
from agents.base_expert import BaseExpert

class BattleManager:
    def __init__(self, agents: List[BaseExpert] = None):
        """Initialize BattleManager with optional list of agents"""
        self.agents = agents or []
        self.problem = ""
        self.current_round = 0
        self.thought_process = []
        self.full_conversation = []

    def add_agent(self, agent: BaseExpert):
        """Add an agent to the battle"""
        self.agents.append(agent)

    def clear_state(self):
        """Clear the battle state"""
        self.problem = ""
        self.current_round = 0
        self.thought_process = []
        self.full_conversation = []
        for agent in self.agents:
            agent.conversation_history = []
            agent.interaction_history = []

    def run_battle(self, problem: str) -> Dict[str, Dict[str, List[str]]]:
        """Run a battle with all agents and return structured analysis"""
        self.clear_state()
        self.problem = problem
        battle_results = {}

        for agent in self.agents:
            # Get agent's analysis
            analysis = agent.generate_analysis(problem)
            
            # Store structured results
            battle_results[agent.name] = {
                "pros": analysis.get("pros", []),
                "cons": analysis.get("cons", []),
                "risks": analysis.get("risks", []),
                "suggestions": analysis.get("suggestions", [])
            }

        return battle_results

    def run_battle_with_rebuttals(self, problem: str, max_rounds: int = 3) -> Dict[str, Dict[str, Any]]:
        """Run a battle with multiple rounds of rebuttals"""
        self.clear_state()
        self.problem = problem
        results = {}
        
        # Initialize results structure for each agent
        for agent in self.agents:
            results[agent.name] = {
                "analysis": agent.generate_analysis(problem),
                "rebuttals": {"Round 1": []},
                "thought_process": []
            }
            # Add initial thought process
            results[agent.name]["thought_process"].extend(results[agent.name]["analysis"].get("thought_process", []))
        
        # Check if any agent needs clarification
        for agent in self.agents:
            if agent.needs_clarification():
                return {
                    "status": "needs_clarification",
                    "questions": agent.get_clarifying_questions(),
                    "agent": agent.name,
                    "current_results": results
                }
        
        # Run rebuttal rounds
        for round_num in range(1, max_rounds + 1):
            self.current_round = round_num
            round_key = f"Round {round_num}"
            
            # If this is not the first round, initialize the round
            if round_num > 1:
                for agent in self.agents:
                    if round_key not in results[agent.name]["rebuttals"]:
                        results[agent.name]["rebuttals"][round_key] = []
            
            # Collect rebuttals from each agent
            for agent in self.agents:
                other_analyses = {
                    other.name: other.generate_analysis(problem)
                    for other in self.agents
                    if other != agent
                }
                
                rebuttal = agent.generate_rebuttal(other_analyses)
                
                # Add thought process to results
                results[agent.name]["thought_process"].extend(rebuttal.get("thought_process", []))
                
                # Ensure rebuttal is properly structured
                if isinstance(rebuttal, list):
                    results[agent.name]["rebuttals"][round_key] = rebuttal
                elif isinstance(rebuttal, dict):
                    # Convert dict rebuttal to list of strings
                    rebuttal_list = []
                    for key, value in rebuttal.items():
                        if key != "thought_process":  # Skip thought process as it's already added
                            if isinstance(value, list):
                                rebuttal_list.extend(value)
                            else:
                                rebuttal_list.append(str(value))
                    results[agent.name]["rebuttals"][round_key] = rebuttal_list
                else:
                    # Handle string rebuttal
                    results[agent.name]["rebuttals"][round_key] = [str(rebuttal)]
            
            # After each round, check if any agent needs clarification
            for agent in self.agents:
                if agent.needs_clarification():
                    return {
                        "status": "needs_clarification",
                        "questions": agent.get_clarifying_questions(),
                        "agent": agent.name,
                        "current_results": results,
                        "round": round_num
                    }
        
        # Add final thought process summary
        for agent in self.agents:
            results[agent.name]["thought_process"].append(
                f"{agent.name} completed all rounds of analysis and rebuttals"
            )
        
        return {
            "status": "completed",
            "results": results
        }

    def get_thought_process(self) -> List[str]:
        """Get the complete thought process"""
        return self.thought_process

    def get_full_conversation(self) -> List[Dict[str, Any]]:
        """Get the complete conversation history"""
        return self.full_conversation 