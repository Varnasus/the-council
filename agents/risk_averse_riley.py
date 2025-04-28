from .base_expert import BaseExpert
from typing import Dict, Any, List

class RiskAverseRiley(BaseExpert):
    def __init__(self, name: str = "Risk-Averse Riley", config: Dict[str, Any] = None):
        super().__init__(name, config)

    def analyze_problem(self, problem: str) -> Dict[str, Any]:
        """Analyze the problem from a risk-averse perspective"""
        # Extract key components from the problem
        problem_lower = problem.lower()
        
        # Initialize analysis structure
        analysis = {
            "technical_risks": {},
            "business_risks": {},
            "security_risks": {}
        }
        
        # Analyze technical risks
        if any(word in problem_lower for word in ["ai", "ml", "smart", "intelligent"]):
            analysis["technical_risks"]["complexity"] = "High risk due to AI complexity and potential for unexpected behavior"
            analysis["technical_risks"]["reliability"] = "Concerns about AI model reliability and consistency"
            analysis["technical_risks"]["maintenance"] = "Significant maintenance overhead for AI systems"
        elif any(word in problem_lower for word in ["real-time", "live", "instant"]):
            analysis["technical_risks"]["complexity"] = "High risk due to real-time processing requirements"
            analysis["technical_risks"]["reliability"] = "Critical reliability concerns for real-time systems"
            analysis["technical_risks"]["maintenance"] = "Complex maintenance requirements for real-time infrastructure"
        else:
            analysis["technical_risks"]["complexity"] = "Standard technical complexity"
            analysis["technical_risks"]["reliability"] = "Standard reliability concerns"
            analysis["technical_risks"]["maintenance"] = "Standard maintenance requirements"
        
        # Analyze business risks
        if any(word in problem_lower for word in ["market", "competition", "growth"]):
            analysis["business_risks"]["market"] = "High risk due to competitive market dynamics"
            analysis["business_risks"]["adoption"] = "Uncertain user adoption rates"
            analysis["business_risks"]["revenue"] = "Unpredictable revenue streams"
        elif any(word in problem_lower for word in ["enterprise", "business", "corporate"]):
            analysis["business_risks"]["market"] = "Enterprise market risks and compliance requirements"
            analysis["business_risks"]["adoption"] = "Complex enterprise adoption process"
            analysis["business_risks"]["revenue"] = "Enterprise sales cycle risks"
        else:
            analysis["business_risks"]["market"] = "Standard market risks"
            analysis["business_risks"]["adoption"] = "Standard adoption risks"
            analysis["business_risks"]["revenue"] = "Standard revenue risks"
        
        # Analyze security risks
        if any(word in problem_lower for word in ["data", "privacy", "security"]):
            analysis["security_risks"]["data"] = "High risk due to sensitive data handling"
            analysis["security_risks"]["compliance"] = "Complex compliance requirements"
            analysis["security_risks"]["access"] = "Critical access control requirements"
        else:
            analysis["security_risks"]["data"] = "Standard data security risks"
            analysis["security_risks"]["compliance"] = "Standard compliance requirements"
            analysis["security_risks"]["access"] = "Standard access control needs"
        
        return analysis

    def generate_solution(self, problem: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a risk-averse solution"""
        technical_analysis = context.get("technical_analysis", {})
        focus_areas = context.get("focus_areas", [])
        biases = context.get("biases", [])
        
        # Extract key components from the problem
        problem_lower = problem.lower()
        
        # Initialize solution structure
        solution = {
            "risk_mitigation": {},
            "implementation_plan": {},
            "security_measures": {},
            "fallback_strategies": {}
        }
        
        # Generate risk mitigation based on problem type
        if any(word in problem_lower for word in ["ai", "ml", "smart"]):
            solution["risk_mitigation"] = {
                "technical": [
                    "Phased AI implementation with human oversight",
                    "Extensive testing and validation framework",
                    "Clear AI decision boundaries and fallbacks"
                ],
                "business": [
                    "Gradual market introduction",
                    "Clear value proposition",
                    "Strong customer support"
                ],
                "security": [
                    "Data anonymization",
                    "Model security measures",
                    "Access control"
                ]
            }
        elif any(word in problem_lower for word in ["real-time", "live", "instant"]):
            solution["risk_mitigation"] = {
                "technical": [
                    "Redundant systems",
                    "Graceful degradation",
                    "Comprehensive monitoring"
                ],
                "business": [
                    "Staged rollout",
                    "User education",
                    "Support infrastructure"
                ],
                "security": [
                    "Real-time monitoring",
                    "Access controls",
                    "Data encryption"
                ]
            }
        else:
            solution["risk_mitigation"] = {
                "technical": [
                    "Standard testing",
                    "Code review",
                    "Documentation"
                ],
                "business": [
                    "Market research",
                    "User feedback",
                    "Support plan"
                ],
                "security": [
                    "Basic security",
                    "Access control",
                    "Data protection"
                ]
            }
        
        # Generate implementation plan based on problem type
        if any(word in problem_lower for word in ["ai", "ml", "smart"]):
            solution["implementation_plan"] = {
                "phases": [
                    "Research and planning",
                    "Prototype development",
                    "Limited pilot",
                    "Full deployment"
                ],
                "timeline": "Extended timeline for proper testing",
                "resources": "Dedicated AI team with oversight"
            }
        elif any(word in problem_lower for word in ["real-time", "live", "instant"]):
            solution["implementation_plan"] = {
                "phases": [
                    "Infrastructure setup",
                    "Core development",
                    "Testing and optimization",
                    "Gradual rollout"
                ],
                "timeline": "Careful timeline with buffer for issues",
                "resources": "Experienced real-time development team"
            }
        else:
            solution["implementation_plan"] = {
                "phases": [
                    "Planning",
                    "Development",
                    "Testing",
                    "Deployment"
                ],
                "timeline": "Standard development timeline",
                "resources": "Standard development team"
            }
        
        # Generate security measures based on problem type
        if any(word in problem_lower for word in ["data", "privacy", "security"]):
            solution["security_measures"] = {
                "data_protection": [
                    "Encryption at rest and in transit",
                    "Access controls",
                    "Audit logging"
                ],
                "compliance": [
                    "Regular audits",
                    "Documentation",
                    "Training"
                ],
                "monitoring": [
                    "Real-time alerts",
                    "Log analysis",
                    "Incident response"
                ]
            }
        else:
            solution["security_measures"] = {
                "data_protection": [
                    "Basic encryption",
                    "Access controls",
                    "Logging"
                ],
                "compliance": [
                    "Standard compliance",
                    "Documentation",
                    "Training"
                ],
                "monitoring": [
                    "Basic monitoring",
                    "Log review",
                    "Incident handling"
                ]
            }
        
        # Generate fallback strategies based on problem type
        if any(word in problem_lower for word in ["ai", "ml", "smart"]):
            solution["fallback_strategies"] = {
                "technical": [
                    "Human-in-the-loop fallback",
                    "Simplified decision trees",
                    "Manual override options"
                ],
                "business": [
                    "Traditional methods as backup",
                    "Customer support escalation",
                    "Service level agreements"
                ],
                "operational": [
                    "Manual processes",
                    "Alternative workflows",
                    "Emergency procedures"
                ]
            }
        else:
            solution["fallback_strategies"] = {
                "technical": [
                    "Basic fallback systems",
                    "Manual processes",
                    "Emergency procedures"
                ],
                "business": [
                    "Alternative solutions",
                    "Support escalation",
                    "Service agreements"
                ],
                "operational": [
                    "Manual workflows",
                    "Backup systems",
                    "Emergency plans"
                ]
            }
        
        return solution

    def generate_rebuttal(self, other_analysis: Dict[str, List[str]]) -> str:
        """Generate security-focused rebuttals"""
        concerns = []
        
        for agent, analysis in other_analysis.items():
            if agent == self.name:
                continue
                
            if "Pragmatic Pete" in agent:
                if any("faster" in s.lower() for s in analysis.get("pros", [])):
                    concerns.append("While speed to market is important, proper security measures cannot be rushed")
                    
            if "Innovative Izzy" in agent:
                if any("real-time" in s.lower() for s in analysis.get("pros", [])):
                    concerns.append("Real-time webhook systems introduce significant security challenges that need careful consideration")
                    
            if "Scalable Sam" in agent:
                if any("distributed" in s.lower() for s in analysis.get("pros", [])):
                    concerns.append("Distributed webhook systems increase the attack surface and complicate security monitoring")
                    
            if "Senior Dev Sam" in agent:
                if any("complexity" in s.lower() for s in analysis.get("cons", [])):
                    concerns.append("The additional complexity of webhook security is a significant risk factor that supports an API-first approach")
        
        if not concerns:
            return "From a security perspective, an API-first approach provides better control over authentication, authorization, and data access patterns."
        
        return ". ".join(concerns) + "."

    def generate_analysis(self, problem: str) -> Dict[str, List[str]]:
        """Generate a structured analysis with pros, cons, risks, and suggestions"""
        analysis = super().generate_analysis(problem)
        
        # Add specific risk-focused analysis
        analysis["pros"].extend([
            "High system reliability and stability",
            "Strong security posture",
            "Comprehensive error handling",
            "Proven technology stack"
        ])
        
        analysis["cons"].extend([
            "Potentially slower development pace",
            "More complex implementation",
            "Higher initial resource requirements",
            "Limited use of cutting-edge technologies"
        ])
        
        analysis["risks"].extend([
            "System failures under load",
            "Data consistency issues",
            "Security vulnerabilities",
            "Integration problems"
        ])
        
        analysis["suggestions"].extend([
            "Implement thorough testing strategy",
            "Set up comprehensive monitoring",
            "Create detailed documentation",
            "Establish incident response procedures"
        ])
        
        return analysis 