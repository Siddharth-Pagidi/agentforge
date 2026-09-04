import os

from dotenv import load_dotenv


load_dotenv()

MODEL_PROVIDER = os.getenv(
    "MODEL_PROVIDER",
    "ollama",
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "qwen3:4b",
)

OLLAMA_HOST = os.getenv(
    "OLLAMA_HOST",
    "http://localhost:11434",
)