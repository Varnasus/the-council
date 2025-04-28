# AI Arena

AI Arena is an innovative platform that simulates expert discussions and debates on technical and business problems. It features multiple AI agents with distinct personalities and expertise areas who analyze problems, provide solutions, and engage in structured debates to arrive at well-rounded recommendations.

## Features

- **Expert AI Agents**: Multiple specialized agents with unique personalities and expertise areas
- **Structured Analysis**: Comprehensive problem analysis with pros, cons, risks, and suggestions
- **Dynamic Debates**: Multi-round discussions with rebuttals and thought process tracking
- **Natural Conversation**: Personality-driven responses and natural dialogue flow
- **Interactive CLI**: User-friendly command-line interface for problem submission and analysis
- **Thought Process Tracking**: Detailed logging of agent reasoning and decision-making

## Expert Agents

### Pragmatic Pete
- **Role**: Business & Revenue Strategist
- **Focus Areas**: Monetization strategies, Market fit analysis, Revenue optimization
- **Personality**: Practical, Revenue-driven, Market-focused, ROI-oriented
- **Biases**: Favors proven solutions, Prioritizes immediate business value

### Innovative Izzy
- **Role**: UX & Innovation Strategist
- **Focus Areas**: User experience innovation, Product differentiation, Future-proofing
- **Personality**: Visionary, Risk-taking, User-centric, Forward-thinking
- **Biases**: Favors modern solutions, Prioritizes user experience

### Senior Dev Sam
- **Role**: Technical Architecture Expert
- **Focus Areas**: Technical architecture, System design, Performance optimization
- **Personality**: Technical, Architecture-focused, Detail-oriented, Quality-driven
- **Biases**: Favors technical elegance, Focuses on maintainability

### Risk-Averse Riley
- **Role**: Risk & Churn Prevention Specialist
- **Focus Areas**: Risk assessment, Churn prevention, User retention
- **Personality**: Conservative, Risk-averse, User-focused, Detail-oriented
- **Biases**: Favors proven security patterns, Prioritizes stability

### Scalable Sam
- **Role**: Operations & Scalability Expert
- **Focus Areas**: System scalability, Operational efficiency, Infrastructure optimization
- **Personality**: Systematic, Efficiency-focused, Scale-oriented, Process-driven
- **Biases**: May over-engineer solutions, Focuses on technical optimization

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-arena.git
cd ai-arena
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys and configuration
```

## Usage

### Running the CLI Interface

```bash
python main.py
```

The CLI will prompt you to enter your problem statement. The agents will then:
1. Analyze the problem
2. Generate initial solutions
3. Engage in multi-round discussions
4. Present final recommendations

### Example Problem Statement

```
Should we implement a Progressive Web App (PWA) instead of native mobile apps for our e-commerce platform?
```

### Understanding the Output

The system provides:
- Individual agent analyses
- Multi-round rebuttals
- Thought processes
- Final recommendations
- Clarifying questions when needed

## Project Structure

```
ai-arena/
├── agents/                 # Expert agent implementations
│   ├── base_expert.py     # Base expert class
│   ├── personas/          # Agent personality configurations
│   └── [agent_name].py    # Individual agent implementations
├── battle/                # Battle system
│   ├── battle_manager.py  # Manages agent interactions
│   └── battle_config.yaml # Battle configuration
├── config/                # Configuration files
├── llm/                   # Language model integration
├── ui/                    # User interface components
├── main.py               # Entry point
└── requirements.txt      # Project dependencies
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for providing the language models
- Contributors and maintainers
- Users and testers of the system

## Roadmap

- [ ] Web interface implementation
- [ ] Additional expert agents
- [ ] Enhanced personality traits
- [ ] Integration with more LLM providers
- [ ] Advanced analysis frameworks
- [ ] Real-time collaboration features 