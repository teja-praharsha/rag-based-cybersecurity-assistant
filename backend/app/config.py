import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[1]

load_dotenv(BASE_DIR / ".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

MODEL_PATH = BASE_DIR / "models" / "cybersecurity_model.joblib"
ENCODER_PATH = BASE_DIR / "models" / "label_encoder.joblib"

PROCESSED_DATA_PATH = (
    BASE_DIR / "data" / "processed" / "CIC-IDS2017-cleaned-combined.csv"
)

CHROMA_PATH = BASE_DIR / "data" / "chroma_db"

KNOWLEDGE_BASE_PATH = BASE_DIR / "data" / "knowledge_base"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

TOP_K_RESULTS = 5