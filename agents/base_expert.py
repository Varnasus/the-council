from abc import ABC, abstractmethod
from typing import Dict, Any, List
import yaml
import os
import logging

# Set up logging with INFO level
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BaseExpert(ABC):
    def __init__(self, name: str, config: Dict[str, Any] = None):
        self.name = name
        self.config = config or {}
        
        # Initialize from config with type checking
        self.focus_areas = self.config.get('focus_areas', [])
        if not isinstance(self.focus_areas, list):
            self.focus_areas = []
        
        self.biases = self.config.get('biases', [])
        if not isinstance(self.biases, list):
            self.biases = []
        
        # Handle analysis framework with type checking
        framework = self.config.get('analysis_framework', [])
        if isinstance(framework, dict):
            self.analysis_framework = list(framework.keys())
        elif isinstance(framework, list):
            self.analysis_framework = framework
        else:
            self.analysis_framework = []
        
        self.persona = self._get_persona()
        self.conversation_history: List[Dict[str, str]] = []
        self.interaction_history: List[Dict[str, Any]] = []
        self.current_round = 0
        self._needs_clarification = False
        self.clarifying_questions = []

    def _get_persona(self) -> Dict[str, Any]:
        """Get the persona configuration"""
        return {
            "name": self.name,
            "focus_areas": self.focus_areas,
            "biases": self.biases,
            "analysis_framework": self.analysis_framework,
            "conversation_style": self.config.get("conversation_style", "professional"),
            "tone": self.config.get("tone", "balanced"),
            "response_length": self.config.get("response_length", "medium"),
            "technical_depth": self.config.get("technical_depth", "moderate")
        }

    @abstractmethod
    def analyze_problem(self, problem: str) -> Dict[str, Any]:
        """Base method for analyzing a problem"""
        pass

    @abstractmethod
    def generate_solution(self, problem: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Base method for generating a solution"""
        pass

    def generate_analysis(self, problem: str) -> Dict[str, List[str]]:
        """Generate a structured analysis with pros, cons, risks, and suggestions"""
        # Clear history before new analysis
        self.conversation_history = []
        self.interaction_history = []
        self.current_round = 0
        self._needs_clarification = False
        self.clarifying_questions = []
        
        # Initialize analysis structure
        analysis = {
            "pros": [],
            "cons": [],
            "risks": [],
            "suggestions": [],
            "clarifying_questions": [],
            "summary": [],
            "thought_process": []
        }
        
        # Add initial thought process
        analysis["thought_process"].append(f"{self.name} is analyzing the problem: {problem}")
        
        # Check if we need more information
        if len(problem.split()) < 10:  # Simple heuristic for insufficient detail
            self._needs_clarification = True
            analysis["clarifying_questions"].append("Could you provide more details about your specific requirements?")
            analysis["clarifying_questions"].append("What are your key objectives and constraints?")
            analysis["clarifying_questions"].append("What is your target timeline and budget?")
            analysis["thought_process"].append(f"{self.name} needs more information to provide a thorough analysis")
            return analysis
            
        # Get technical analysis
        technical_analysis = self.analyze_problem(problem)
        analysis["thought_process"].append(f"{self.name} completed technical analysis: {technical_analysis}")
        
        # Generate solution with context
        context = {
            "technical_analysis": technical_analysis,
            "persona": self.persona,
            "focus_areas": self.focus_areas,
            "biases": self.biases,
            "analysis_framework": self.analysis_framework,
            "current_round": self.current_round
        }
        
        solution = self.generate_solution(problem, context)
        analysis["thought_process"].append(f"{self.name} generated initial solution based on technical analysis")
        
        # Add persona-specific insights based on the problem context
        if "Pragmatic Pete" in self.name:
            analysis["pros"].append("Strong focus on business value and ROI")
            analysis["suggestions"].append("Consider implementing a phased approach to validate business impact")
            analysis["suggestions"].append("Start with a minimum viable product to test market fit")
            analysis["thought_process"].append(f"{self.name} added business-focused insights")
        
        elif "Innovative Izzy" in self.name:
            analysis["pros"].append("Forward-thinking approach to product development")
            analysis["suggestions"].append("Explore innovative features that could provide competitive advantage")
            analysis["suggestions"].append("Consider user experience and engagement strategies")
            analysis["thought_process"].append(f"{self.name} added innovation-focused insights")
        
        elif "Senior Dev Sam" in self.name:
            analysis["pros"].append("Technical excellence and scalability considerations")
            analysis["suggestions"].append("Implement robust testing and monitoring from the start")
            analysis["suggestions"].append("Focus on maintainable and scalable architecture")
            analysis["thought_process"].append(f"{self.name} added technical-focused insights")
        
        # Add summary based on persona's focus areas and biases
        focus_areas = self.focus_areas or self.persona.get("focus_areas", [])
        biases = self.biases or self.persona.get("biases", [])
        
        summary = f"Summary ({self.name}): "
        if focus_areas:
            summary += f"Focusing on {', '.join(focus_areas)}, "
        if biases:
            summary += f"with biases towards {', '.join(biases)}. "
            
        # Add key recommendation
        if analysis["suggestions"]:
            summary += f"Key recommendation: {analysis['suggestions'][0]}"
            
        analysis["summary"] = [summary]
        analysis["thought_process"].append(f"{self.name} completed analysis with summary: {summary}")
        
        return analysis

    def generate_rebuttal(self, other_analysis: Dict[str, Dict[str, List[str]]]) -> Dict[str, List[str]]:
        """Generate a rebuttal to another agent's analysis"""
        self.current_round += 1
        
        # Initialize rebuttal structure
        rebuttal = {
            "pros": [],
            "cons": [],
            "risks": [],
            "suggestions": [],
            "thought_process": []
        }
        
        rebuttal["thought_process"].append(f"{self.name} is preparing rebuttal for round {self.current_round}")
        
        # Analyze each other agent's analysis
        for agent_name, analysis in other_analysis.items():
            rebuttal["thought_process"].append(f"{self.name} analyzing {agent_name}'s points")
            
            # Extract key points from their analysis
            their_pros = analysis.get("pros", [])
            their_cons = analysis.get("cons", [])
            their_risks = analysis.get("risks", [])
            their_suggestions = analysis.get("suggestions", [])
            
            # Generate rebuttal based on persona and focus areas
            if "Pragmatic Pete" in self.name:
                # Business-focused rebuttals
                for pro in their_pros:
                    if "market" in pro.lower() or "revenue" in pro.lower():
                        rebuttal["cons"].append(f"While {pro} is important, we should consider the business implications")
                for con in their_cons:
                    if "cost" in con.lower() or "investment" in con.lower():
                        rebuttal["pros"].append(f"Despite {con}, the long-term business value justifies the investment")
                for risk in their_risks:
                    if "market" in risk.lower() or "customer" in risk.lower():
                        rebuttal["suggestions"].append(f"To mitigate {risk}, we should implement a phased market approach")
            
            elif "Innovative Izzy" in self.name:
                # Innovation-focused rebuttals
                for pro in their_pros:
                    if "technical" in pro.lower() or "feature" in pro.lower():
                        rebuttal["pros"].append(f"{pro} demonstrates the potential for innovative solutions")
                for con in their_cons:
                    if "complexity" in con.lower() or "difficulty" in con.lower():
                        rebuttal["suggestions"].append(f"To address {con}, we can implement innovative user-friendly solutions")
                for risk in their_risks:
                    if "technical" in risk.lower() or "implementation" in risk.lower():
                        rebuttal["pros"].append(f"While {risk} exists, it presents an opportunity for creative problem-solving")
            
            elif "Senior Dev Sam" in self.name:
                # Technical-focused rebuttals
                for pro in their_pros:
                    if "technical" in pro.lower() or "architecture" in pro.lower():
                        rebuttal["pros"].append(f"{pro} aligns with best technical practices")
                for con in their_cons:
                    if "technical" in con.lower() or "implementation" in con.lower():
                        rebuttal["suggestions"].append(f"To overcome {con}, we should follow established technical patterns")
                for risk in their_risks:
                    if "technical" in risk.lower() or "system" in risk.lower():
                        rebuttal["cons"].append(f"{risk} requires careful technical consideration")
        
        # If no rebuttals were generated, add a default message
        if not any(rebuttal.values()):
            rebuttal["suggestions"].append(f"{self.name} has no specific rebuttals to make at this time.")
            rebuttal["thought_process"].append(f"{self.name} found no specific points to rebut")
        else:
            rebuttal["thought_process"].append(f"{self.name} completed rebuttal with {len(rebuttal['pros'])} pros, {len(rebuttal['cons'])} cons, and {len(rebuttal['suggestions'])} suggestions")
        
        return rebuttal

    def add_to_history(self, role: str, content: str):
        """Add a message to the conversation history"""
        self.conversation_history.append({
            "role": role,
            "content": content,
            "round": self.current_round
        })

    def get_history(self) -> List[Dict[str, str]]:
        """Get the conversation history"""
        return self.conversation_history

    def needs_clarification(self) -> bool:
        """Check if the agent needs clarification"""
        return self._needs_clarification

    def get_clarifying_questions(self) -> List[str]:
        """Get the list of clarifying questions"""
        return self.clarifying_questions

    def respond_to_point(self, point: str, agent_name: str) -> str:
        """Respond to a specific point made by another agent"""
        # Add the point to interaction history
        self.interaction_history.append({
            "agent": agent_name,
            "point": point,
            "timestamp": len(self.interaction_history),
            "round": self.current_round
        })
        
        # Generate response based on persona and point
        response = f"{self.name} responds to {agent_name}'s point: "
        
        # Generate response based on focus areas and persona
        focus_areas = self.focus_areas or self.persona.get("focus_areas", [])
        
        if "Pragmatic Pete" in self.name:
            response += f"Considering the business impact and market value, {point} requires careful evaluation of ROI and market fit."
        elif "Innovative Izzy" in self.name:
            response += f"From an innovation standpoint, {point} presents opportunities for enhancing user experience and product differentiation."
        elif "Risk-Averse Riley" in self.name:
            response += f"We need to carefully assess the risks and stability implications of {point}."
        elif "Scalable Sam" in self.name:
            response += f"Looking at scalability and performance aspects, {point} needs architectural consideration."
        elif "Senior Dev Sam" in self.name:
            response += f"From a technical perspective, {point} requires focus on maintainability and system design."
        
        # Add focus area context if relevant
        if focus_areas:
            response += f" Key considerations include: {', '.join(focus_areas)}."
        
        return response

    def _generate_area_insights(self, area: str, framework: str, solution: Dict[str, Any], aspect: str) -> List[str]:
        """Generate specific insights for an area based on the solution and framework"""
        insights = []
        
        # Extract relevant parts of the solution based on the aspect
        if aspect == "positive":
            if "benefits" in solution:
                insights.extend([f"{area}: {benefit}" for benefit in solution["benefits"]])
        elif aspect == "negative":
            if "challenges" in solution:
                insights.extend([f"{area}: {challenge}" for challenge in solution["challenges"]])
        elif aspect == "risk":
            if "risks" in solution:
                insights.extend([f"{area}: {risk}" for risk in solution["risks"]])
        elif aspect == "action":
            if "recommendations" in solution:
                insights.extend([f"{area}: {rec}" for rec in solution["recommendations"]])
        
        # Add the framework-based insight if no specific insights were found
        if not insights:
            insights.append(f"{area}: {framework}")
        
        return insights 