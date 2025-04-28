from .base_expert import BaseExpert
from typing import Dict, Any, List

class PragmaticPete(BaseExpert):
    def __init__(self, name: str = "Pragmatic Pete", config: Dict[str, Any] = None):
        super().__init__(name, config)

    def analyze_problem(self, problem: str) -> Dict[str, Any]:
        """Analyze the problem from a business perspective"""
        # Initialize analysis structure
        analysis = {
            "business_impact": {},
            "cost_benefit": {},
            "implementation": {}
        }
        
        # Analyze based on actual problem content
        analysis["business_impact"] = {
            "market_opportunity": self._analyze_market_opportunity(problem),
            "competitive_advantage": self._analyze_competitive_advantage(problem),
            "revenue_potential": self._analyze_revenue_potential(problem),
            "customer_adoption": self._analyze_customer_adoption(problem)
        }
        
        analysis["cost_benefit"] = {
            "development_costs": self._analyze_development_costs(problem),
            "maintenance_costs": self._analyze_maintenance_costs(problem),
            "roi_timeline": self._analyze_roi_timeline(problem)
        }
        
        analysis["implementation"] = {
            "complexity": self._analyze_implementation_complexity(problem),
            "timeline": self._analyze_timeline(problem),
            "resources": self._analyze_resource_needs(problem)
        }
        
        return analysis
        
    def _analyze_market_opportunity(self, problem: str) -> str:
        """Analyze market opportunity based on the problem"""
        return f"Market opportunity analysis based on: {problem}"
        
    def _analyze_competitive_advantage(self, problem: str) -> str:
        """Analyze competitive advantage based on the problem"""
        return f"Competitive advantage analysis based on: {problem}"
        
    def _analyze_revenue_potential(self, problem: str) -> str:
        """Analyze revenue potential based on the problem"""
        return f"Revenue potential analysis based on: {problem}"
        
    def _analyze_customer_adoption(self, problem: str) -> str:
        """Analyze customer adoption potential based on the problem"""
        return f"Customer adoption analysis based on: {problem}"
        
    def _analyze_development_costs(self, problem: str) -> str:
        """Analyze development costs based on the problem"""
        return f"Development cost analysis based on: {problem}"
        
    def _analyze_maintenance_costs(self, problem: str) -> str:
        """Analyze maintenance costs based on the problem"""
        return f"Maintenance cost analysis based on: {problem}"
        
    def _analyze_roi_timeline(self, problem: str) -> str:
        """Analyze ROI timeline based on the problem"""
        return f"ROI timeline analysis based on: {problem}"
        
    def _analyze_implementation_complexity(self, problem: str) -> str:
        """Analyze implementation complexity based on the problem"""
        return f"Implementation complexity analysis based on: {problem}"
        
    def _analyze_timeline(self, problem: str) -> str:
        """Analyze timeline based on the problem"""
        return f"Timeline analysis based on: {problem}"
        
    def _analyze_resource_needs(self, problem: str) -> str:
        """Analyze resource needs based on the problem"""
        return f"Resource needs analysis based on: {problem}"

    def generate_solution(self, problem: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a business-focused solution"""
        technical_analysis = context.get("technical_analysis", {})
        focus_areas = context.get("focus_areas", [])
        biases = context.get("biases", [])
        
        # Extract key components from the problem
        problem_lower = problem.lower()
        
        # Initialize solution structure
        solution = {
            "implementation_plan": {},
            "cost_estimates": {},
            "timeline": {},
            "key_metrics": {},
            "monetization": {}
        }
        
        # Generate implementation plan based on complexity
        if "complex" in technical_analysis.get("implementation", {}).get("complexity", "").lower():
            solution["implementation_plan"] = {
                "phase1": "Requirements gathering and architecture design",
                "phase2": "Core functionality development",
                "phase3": "Integration and testing",
                "phase4": "Beta release and feedback collection",
                "phase5": "Full launch and marketing"
            }
        else:
            solution["implementation_plan"] = {
                "phase1": "MVP development",
                "phase2": "User testing and feedback",
                "phase3": "Feature refinement",
                "phase4": "Launch and initial marketing"
            }
        
        # Generate cost estimates based on complexity
        if "significant" in technical_analysis.get("cost_benefit", {}).get("development_costs", "").lower():
            solution["cost_estimates"] = {
                "development": "$200k - $300k",
                "marketing": "$75k - $100k",
                "operations": "$40k/month",
                "support": "$25k/month"
            }
        else:
            solution["cost_estimates"] = {
                "development": "$100k - $150k",
                "marketing": "$50k - $75k",
                "operations": "$25k/month",
                "support": "$15k/month"
            }
        
        # Generate timeline based on complexity
        if "complex" in technical_analysis.get("implementation", {}).get("complexity", "").lower():
            solution["timeline"] = {
                "planning": "4 weeks",
                "development": "12 weeks",
                "testing": "6 weeks",
                "launch": "4 weeks"
            }
        else:
            solution["timeline"] = {
                "planning": "2 weeks",
                "development": "8 weeks",
                "testing": "4 weeks",
                "launch": "2 weeks"
            }
        
        # Generate key metrics based on market opportunity
        if "significant" in technical_analysis.get("business_impact", {}).get("market_opportunity", "").lower():
            solution["key_metrics"] = {
                "mrr_target": "$200k within 6 months",
                "customer_target": "200 paying customers",
                "growth_rate": "20% MoM",
                "churn_rate": "<5% monthly"
            }
        else:
            solution["key_metrics"] = {
                "mrr_target": "$100k within 6 months",
                "customer_target": "100 paying customers",
                "growth_rate": "10% MoM",
                "churn_rate": "<3% monthly"
            }
        
        # Generate monetization strategy based on revenue potential
        if "recurring" in technical_analysis.get("business_impact", {}).get("revenue_potential", "").lower():
            solution["monetization"] = {
                "pricing_tiers": [
                    "Free: Basic features",
                    "Basic: $49/month",
                    "Pro: $149/month",
                    "Enterprise: Custom pricing"
                ],
                "revenue_streams": [
                    "Subscription fees",
                    "Premium features",
                    "Professional services",
                    "Training and support"
                ]
            }
        else:
            solution["monetization"] = {
                "pricing_tiers": [
                    "Basic: $99 one-time",
                    "Pro: $299 one-time",
                    "Enterprise: Custom pricing"
                ],
                "revenue_streams": [
                    "One-time purchases",
                    "Premium support",
                    "Custom development",
                    "Training services"
                ]
            }
        
        return solution

    def generate_analysis(self, problem: str) -> Dict[str, List[str]]:
        """Generate a structured analysis with pros, cons, risks, and suggestions"""
        analysis = super().generate_analysis(problem)
        
        # Add specific business-focused analysis
        analysis["pros"].extend([
            "Strong market demand for API integration solutions",
            "Clear path to monetization through tiered pricing",
            "Low maintenance costs post-implementation",
            "Scalable business model with recurring revenue potential"
        ])
        
        analysis["cons"].extend([
            "Initial development costs may be high",
            "Requires significant customer education",
            "Competitive market with established players",
            "Integration complexity may increase support costs"
        ])
        
        analysis["risks"].extend([
            "Market adoption may be slower than expected",
            "Integration challenges with existing systems",
            "Pricing pressure from competitors",
            "Customer churn due to complexity"
        ])
        
        analysis["suggestions"].extend([
            "Start with a limited feature set to validate market fit",
            "Implement usage-based pricing to align with customer value",
            "Develop comprehensive documentation and support materials",
            "Create a partner program to accelerate adoption"
        ])
        
        return analysis

    def generate_rebuttal(self, other_analysis: Dict[str, Dict[str, List[str]]]) -> Dict[str, List[str]]:
        """Generate a rebuttal to another agent's analysis"""
        # Initialize rebuttal structure
        rebuttal = {
            "pros": [],
            "cons": [],
            "risks": [],
            "suggestions": []
        }
        
        # Analyze each other agent's analysis
        for agent_name, analysis in other_analysis.items():
            # Extract key points from their analysis
            their_pros = analysis.get("pros", [])
            their_cons = analysis.get("cons", [])
            their_risks = analysis.get("risks", [])
            their_suggestions = analysis.get("suggestions", [])
            
            # Generate rebuttal based on actual analysis content
            for pro in their_pros:
                rebuttal["cons"].append(f"While {pro} is valuable, we should consider the business impact")
            
            for con in their_cons:
                rebuttal["pros"].append(f"Despite {con}, the business benefits justify the approach")
            
            for risk in their_risks:
                rebuttal["suggestions"].append(f"To address {risk}, we should implement proper business safeguards")
            
            for suggestion in their_suggestions:
                rebuttal["suggestions"].append(f"Building on {suggestion}, we should also consider business best practices")
        
        # If no rebuttals were generated, add a default message
        if not any(rebuttal.values()):
            rebuttal["suggestions"].append(f"{self.name} has no specific rebuttals to make at this time.")
        
        return rebuttal 