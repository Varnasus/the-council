import os
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Model configurations
MODEL_CONFIGS: Dict[str, Dict[str, Any]] = {
    "gpt-4-mini": {
        "temperature": float(os.getenv("TEMPERATURE", "0.7")),
        "max_tokens": int(os.getenv("MAX_TOKENS", "1000")),
        "top_p": 1.0,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0
    },
    "gpt-4": {
        "temperature": float(os.getenv("TEMPERATURE", "0.7")),
        "max_tokens": int(os.getenv("MAX_TOKENS", "2000")),
        "top_p": 1.0,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0
    },
    "gpt-3.5-turbo": {
        "temperature": float(os.getenv("TEMPERATURE", "0.7")),
        "max_tokens": int(os.getenv("MAX_TOKENS", "1000")),
        "top_p": 1.0,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0
    }
}

# Default model to use
DEFAULT_MODEL = os.getenv("MODEL_NAME", "gpt-4-mini")

# API settings
API_TIMEOUT = 30  # seconds
MAX_RETRIES = 3

# Battle settings
MAX_ROUNDS = 3
MIN_SOLUTION_LENGTH = 100
MAX_SOLUTION_LENGTH = 2000 