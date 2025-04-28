# AI Arena - Multi-Agent Problem Solving Platform

AI Arena is a platform where multiple AI agents with different expertise collaborate to solve complex problems. Each agent brings a unique perspective to the problem, providing diverse solutions and insights.

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your OpenAI API key:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

## Usage

Run the application:
```bash
python main.py
```

Enter your problem statement when prompted, and the agents will analyze and provide solutions from their respective perspectives.

## Agents

- **Pragmatic Pete**: Business-focused expert emphasizing ROI, scalability, and practical implementation
- **Innovative Izzy**: Innovation-focused expert emphasizing creative and cutting-edge solutions
- **Senior Dev Sam**: Technical expert focusing on architecture, implementation, and best practices

## Project Structure

```
/agents
  /base_expert.py        # Shared base agent
  /pragmatic_pete.py     # Business-focused expert
  /innovative_izzy.py    # Innovation-focused expert
  /senior_dev_sam.py     # Senior developer expert

/battle
  /battle_manager.py     # Coordinates agents and flow

/config
  /settings.py           # Model configurations

/llm
  /llm_client.py         # LLM access abstraction

/ui
  /cli_interface.py      # CLI interface

/frontend
  # React project (coming soon)

INSTRUCTIONS.md
cursor-rules.json
main.py                 # Python entrypoint
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License 