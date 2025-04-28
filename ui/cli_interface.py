from typing import Dict, Any
from battle.battle_manager import BattleManager
from agents.pragmatic_pete import PragmaticPete
from agents.innovative_izzy import InnovativeIzzy
from agents.senior_dev_sam import SeniorDevSam

class CLIInterface:
    def __init__(self):
        self.battle_manager = BattleManager()
        self._initialize_agents()

    def _initialize_agents(self):
        """Initialize all agents"""
        self.battle_manager.add_agent(PragmaticPete())
        self.battle_manager.add_agent(InnovativeIzzy())
        self.battle_manager.add_agent(SeniorDevSam())

    def start(self):
        """Start the CLI interface"""
        print("Welcome to AI Arena!")
        print("Enter your problem statement (or 'quit' to exit):")
        
        while True:
            problem = input("> ")
            if problem.lower() == 'quit':
                break

            print("\nRunning battle...")
            results = self.battle_manager.run_battle_with_rebuttals(problem)
            
            if results.get("status") == "needs_clarification":
                self._handle_clarification(results)
            else:
                self._display_results(results["results"])

    def _handle_clarification(self, results: Dict[str, Any]):
        """Handle agent's request for clarification"""
        agent = results["agent"]
        questions = results["questions"]
        current_results = results.get("current_results", {})
        
        print(f"\n{agent} needs clarification:")
        for i, question in enumerate(questions, 1):
            print(f"{i}. {question}")
        
        print("\nPlease provide additional information (or 'skip' to continue):")
        additional_info = input("> ")
        
        if additional_info.lower() != 'skip':
            # Update the problem with additional information
            updated_problem = f"{self.battle_manager.problem}\nAdditional information: {additional_info}"
            new_results = self.battle_manager.run_battle_with_rebuttals(updated_problem)
            
            if new_results.get("status") == "needs_clarification":
                self._handle_clarification(new_results)
            else:
                self._display_results(new_results["results"])
        else:
            # Continue with current results
            self._display_results(current_results)

    def _display_results(self, results: Dict[str, Dict[str, Any]]) -> None:
        """Display battle results in a clean, structured format"""
        for agent_name, agent_results in results.items():
            print(f"\n=== {agent_name} ===")
            
            # Display analysis
            analysis = agent_results["analysis"]
            print("\nAnalysis:")
            if analysis.get("pros"):
                print("  Pros:")
                for pro in analysis["pros"]:
                    print(f"    • {pro}")
            
            if analysis.get("cons"):
                print("  Cons:")
                for con in analysis["cons"]:
                    print(f"    • {con}")
            
            if analysis.get("risks"):
                print("  Risks:")
                for risk in analysis["risks"]:
                    print(f"    • {risk}")
            
            if analysis.get("suggestions"):
                print("  Suggestions:")
                for suggestion in analysis["suggestions"]:
                    print(f"    • {suggestion}")
            
            # Display rebuttals
            rebuttals = agent_results.get("rebuttals", {})
            if rebuttals:
                print("\n  Rebuttals:")
                # Sort rounds and display only those with content
                for round_num in sorted(rebuttals.keys(), key=lambda x: int(x.split()[-1])):
                    round_rebuttals = rebuttals[round_num]
                    if round_rebuttals:  # Only display rounds with content
                        print(f"    {round_num}:")
                        for rebuttal in round_rebuttals:
                            print(f"      • {rebuttal}")
            
            # Display thought process
            thought_process = agent_results.get("thought_process", [])
            if thought_process:
                print("\n  Thought Process:")
                for thought in thought_process:
                    print(f"    • {thought}")
            
            print("=" * 50) 