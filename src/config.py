import os

from dotenv import load_dotenv


load_dotenv()


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

MODELO_CHAT = "gemini-3.5-flash"
MODELO_EMBEDDING = "gemini-embedding-001"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150
TOP_K = 5