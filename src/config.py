import os
from dotenv import load_dotenv

load_dotenv()

try:
    import streamlit as st
except ImportError:
    st = None


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY and st is not None:
    try:
        GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass


MODELO_CHAT = "gemini-3.5-flash"
MODELO_EMBEDDING = "gemini-embedding-001"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150
TOP_K = 5