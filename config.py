import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen3:4b")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
DATABASE_PATH = os.getenv("AGENTFORGE_DB", "agentforge.db")
MAX_TEAM_SIZE = int(os.getenv("MAX_TEAM_SIZE", "4"))
