from .base_expert import BaseExpert
from typing import Dict, Any, List

class ScalableSam(BaseExpert):
    def __init__(self, name: str = "Scalable Sam", config: Dict[str, Any] = None):
        super().__init__(name, config)

    def analyze_problem(self, problem: str) -> Dict[str, Any]:
        """Analyze the problem from a scalability perspective"""
        # Extract key components from the problem
        problem_lower = problem.lower()
        
        # Initialize analysis structure
        analysis = {
            "scalability_requirements": {},
            "performance_considerations": {},
            "growth_potential": {}
        }
        
        # Analyze scalability requirements
        if any(word in problem_lower for word in ["ai", "ml", "smart", "intelligent"]):
            analysis["scalability_requirements"]["compute"] = "High compute requirements for AI processing"
            analysis["scalability_requirements"]["storage"] = "Large storage needs for AI models and data"
            analysis["scalability_requirements"]["network"] = "High bandwidth for AI inference"
        elif any(word in problem_lower for word in ["real-time", "live", "instant"]):
            analysis["scalability_requirements"]["compute"] = "High throughput processing requirements"
            analysis["scalability_requirements"]["storage"] = "Efficient real-time data storage"
            analysis["scalability_requirements"]["network"] = "Low latency network requirements"
        else:
            analysis["scalability_requirements"]["compute"] = "Standard compute requirements"
            analysis["scalability_requirements"]["storage"] = "Standard storage needs"
            analysis["scalability_requirements"]["network"] = "Standard network requirements"
        
        # Analyze performance considerations
        if any(word in problem_lower for word in ["enterprise", "business", "corporate"]):
            analysis["performance_considerations"]["load"] = "Enterprise-scale load handling"
            analysis["performance_considerations"]["latency"] = "Low latency requirements"
            analysis["performance_considerations"]["availability"] = "High availability needs"
        elif any(word in problem_lower for word in ["mobile", "app", "user"]):
            analysis["performance_considerations"]["load"] = "Mobile-scale load handling"
            analysis["performance_considerations"]["latency"] = "Mobile-optimized latency"
            analysis["performance_considerations"]["availability"] = "Mobile app availability"
        else:
            analysis["performance_considerations"]["load"] = "Standard load handling"
            analysis["performance_considerations"]["latency"] = "Standard latency requirements"
            analysis["performance_considerations"]["availability"] = "Standard availability needs"
        
        # Analyze growth potential
        if any(word in problem_lower for word in ["market", "growth", "scale"]):
            analysis["growth_potential"]["users"] = "High user growth potential"
            analysis["growth_potential"]["data"] = "Significant data growth expected"
            analysis["growth_potential"]["features"] = "Expanding feature set planned"
        else:
            analysis["growth_potential"]["users"] = "Standard user growth"
            analysis["growth_potential"]["data"] = "Standard data growth"
            analysis["growth_potential"]["features"] = "Standard feature expansion"
        
        return analysis

    def generate_solution(self, problem: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a scalability-focused solution"""
        technical_analysis = context.get("technical_analysis", {})
        focus_areas = context.get("focus_areas", [])
        biases = context.get("biases", [])
        
        # Extract key components from the problem
        problem_lower = problem.lower()
        
        # Initialize solution structure
        solution = {
            "architecture": {},
            "scaling_strategy": {},
            "performance_optimization": {},
            "monitoring": {}
        }
        
        # Generate architecture based on problem type
        if any(word in problem_lower for word in ["ai", "ml", "smart"]):
            solution["architecture"] = {
                "frontend": "React with AI components",
                "backend": "Python with FastAPI and ML libraries",
                "database": "Vector database for AI features",
                "caching": "Redis for AI model caching",
                "messaging": "Kafka for AI event streaming"
            }
        elif any(word in problem_lower for word in ["real-time", "live", "instant"]):
            solution["architecture"] = {
                "frontend": "React with real-time updates",
                "backend": "Node.js with WebSocket support",
                "database": "MongoDB with change streams",
                "caching": "Redis for real-time data",
                "messaging": "WebSocket for instant updates"
            }
        else:
            solution["architecture"] = {
                "frontend": "React with TypeScript",
                "backend": "Node.js with Express",
                "database": "MongoDB for flexibility",
                "caching": "Redis for performance",
                "messaging": "REST API with webhooks"
            }
        
        # Generate scaling strategy based on problem type
        if any(word in problem_lower for word in ["ai", "ml", "smart"]):
            solution["scaling_strategy"] = {
                "horizontal": [
                    "AI model serving clusters",
                    "Data processing workers",
                    "API gateway instances"
                ],
                "vertical": [
                    "GPU-optimized instances",
                    "High-memory nodes",
                    "Fast storage"
                ],
                "auto_scaling": [
                    "Model-based scaling",
                    "Load-based scaling",
                    "Cost-optimized scaling"
                ]
            }
        elif any(word in problem_lower for word in ["real-time", "live", "instant"]):
            solution["scaling_strategy"] = {
                "horizontal": [
                    "WebSocket servers",
                    "Message brokers",
                    "API instances"
                ],
                "vertical": [
                    "High-CPU instances",
                    "Low-latency storage",
                    "Fast networking"
                ],
                "auto_scaling": [
                    "Connection-based scaling",
                    "Message-based scaling",
                    "Latency-based scaling"
                ]
            }
        else:
            solution["scaling_strategy"] = {
                "horizontal": [
                    "API servers",
                    "Database replicas",
                    "Cache nodes"
                ],
                "vertical": [
                    "Standard instances",
                    "Balanced storage",
                    "Standard networking"
                ],
                "auto_scaling": [
                    "CPU-based scaling",
                    "Memory-based scaling",
                    "Request-based scaling"
                ]
            }
        
        # Generate performance optimization based on problem type
        if any(word in problem_lower for word in ["ai", "ml", "smart"]):
            solution["performance_optimization"] = {
                "compute": [
                    "Model optimization",
                    "Batch processing",
                    "GPU acceleration"
                ],
                "storage": [
                    "Data partitioning",
                    "Caching strategies",
                    "Compression"
                ],
                "network": [
                    "CDN integration",
                    "Load balancing",
                    "Connection pooling"
                ]
            }
        elif any(word in problem_lower for word in ["real-time", "live", "instant"]):
            solution["performance_optimization"] = {
                "compute": [
                    "Event batching",
                    "Connection pooling",
                    "Message batching"
                ],
                "storage": [
                    "In-memory caching",
                    "Data sharding",
                    "Index optimization"
                ],
                "network": [
                    "WebSocket optimization",
                    "Load balancing",
                    "Connection management"
                ]
            }
        else:
            solution["performance_optimization"] = {
                "compute": [
                    "Code optimization",
                    "Caching",
                    "Load balancing"
                ],
                "storage": [
                    "Index optimization",
                    "Query optimization",
                    "Caching"
                ],
                "network": [
                    "CDN integration",
                    "Load balancing",
                    "Connection pooling"
                ]
            }
        
        # Generate monitoring based on problem type
        if any(word in problem_lower for word in ["ai", "ml", "smart"]):
            solution["monitoring"] = {
                "metrics": [
                    "Model performance",
                    "Inference latency",
                    "Resource utilization"
                ],
                "alerts": [
                    "Model drift",
                    "Performance degradation",
                    "Resource constraints"
                ],
                "logging": [
                    "Model predictions",
                    "Error tracking",
                    "Resource usage"
                ]
            }
        elif any(word in problem_lower for word in ["real-time", "live", "instant"]):
            solution["monitoring"] = {
                "metrics": [
                    "Connection count",
                    "Message latency",
                    "Throughput"
                ],
                "alerts": [
                    "Connection drops",
                    "Latency spikes",
                    "Message backlog"
                ],
                "logging": [
                    "Connection events",
                    "Message flow",
                    "Error tracking"
                ]
            }
        else:
            solution["monitoring"] = {
                "metrics": [
                    "Request rate",
                    "Response time",
                    "Error rate"
                ],
                "alerts": [
                    "High latency",
                    "Error spikes",
                    "Resource constraints"
                ],
                "logging": [
                    "Request tracking",
                    "Error logging",
                    "Performance metrics"
                ]
            }
        
        return solution

    def generate_analysis(self, problem: str) -> Dict[str, List[str]]:
        """Generate a structured analysis with pros, cons, risks, and suggestions"""
        analysis = super().generate_analysis(problem)
        
        # Add specific scalability-focused analysis
        analysis["pros"].extend([
            "High performance under load",
            "Efficient resource utilization",
            "Future-proof architecture",
            "Cost-effective scaling"
        ])
        
        analysis["cons"].extend([
            "Higher initial complexity",
            "More infrastructure requirements",
            "Increased operational overhead",
            "Higher development costs"
        ])
        
        analysis["risks"].extend([
            "Performance bottlenecks",
            "Scaling limitations",
            "Resource contention",
            "Cost overruns"
        ])
        
        analysis["suggestions"].extend([
            "Implement comprehensive monitoring",
            "Design for horizontal scaling",
            "Optimize database queries",
            "Set up automated scaling"
        ])
        
        return analysis

    def generate_rebuttal(self, other_analysis: Dict[str, List[str]]) -> str:
        """Generate scalability-focused rebuttals"""
        concerns = []
        
        for agent, analysis in other_analysis.items():
            if agent == self.name:
                continue
                
            if "Pragmatic Pete" in agent:
                if any("cost" in s.lower() for s in analysis.get("pros", [])):
                    concerns.append("While initial costs might be lower with APIs, webhook infrastructure costs can be optimized through modern cloud services")
                    
            if "Innovative Izzy" in agent:
                if any("event" in s.lower() for s in analysis.get("pros", [])):
                    concerns.append("Event-driven architectures require significantly more complex infrastructure and scaling considerations")
                    
            if "Risk-Averse Riley" in agent:
                if any("security" in s.lower() for s in analysis.get("pros", [])):
                    concerns.append("The additional infrastructure components needed for webhooks create more potential points of failure")
                    
            if "Senior Dev Sam" in agent:
                if any("maintenance" in s.lower() for s in analysis.get("cons", [])):
                    concerns.append("The operational overhead of maintaining webhook infrastructure can impact system reliability")
        
        if not concerns:
            return "From a scalability perspective, an API-first approach provides better control over system resources and simpler scaling patterns."
        
        return ". ".join(concerns) + "." 