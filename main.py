import os
from dotenv import load_dotenv
from ui.cli_interface import CLIInterface
from llm.llm_client import LLMClient

def main():
    # Load environment variables from .env file
    load_dotenv()
    
    # Initialize LLM client with API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found in environment variables or .env file")
        print("Please create a .env file with your API key or set the environment variable")
        return

    llm_client = LLMClient(api_key)
    
    # Initialize and start CLI interface
    cli = CLIInterface()
    cli.start()

if __name__ == "__main__":
    main() 