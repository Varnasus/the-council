import openai
from typing import Dict, Any, List
from config.settings import MODEL_CONFIGS, DEFAULT_MODEL, API_TIMEOUT, MAX_RETRIES

class LLMClient:
    def __init__(self, api_key: str):
        openai.api_key = api_key
        self.model = DEFAULT_MODEL

    def set_model(self, model: str):
        """Set the model to use"""
        if model in MODEL_CONFIGS:
            self.model = model
        else:
            raise ValueError(f"Model {model} not supported")

    def generate_response(self, messages: List[Dict[str, str]]) -> str:
        """Generate a response from the LLM"""
        config = MODEL_CONFIGS[self.model]
        
        for attempt in range(MAX_RETRIES):
            try:
                response = openai.ChatCompletion.create(
                    model=self.model,
                    messages=messages,
                    temperature=config["temperature"],
                    max_tokens=config["max_tokens"],
                    top_p=config["top_p"],
                    frequency_penalty=config["frequency_penalty"],
                    presence_penalty=config["presence_penalty"]
                )
                return response.choices[0].message.content
            except Exception as e:
                if attempt == MAX_RETRIES - 1:
                    raise e
                continue

    def get_embeddings(self, text: str) -> List[float]:
        """Get embeddings for the given text"""
        response = openai.Embedding.create(
            input=text,
            model="text-embedding-ada-002"
        )
        return response.data[0].embedding 