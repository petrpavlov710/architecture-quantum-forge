import os

from pydantic_settings import BaseSettings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_DIR = os.path.join(BASE_DIR, "app")


class Config(BaseSettings):
    knowledge_dir: str = os.path.join(APP_DIR, "knowledge_base")
    raw_dir: str = os.path.join(APP_DIR, "knowledge_base/raw")
    processed_dir: str = os.path.join(APP_DIR, "knowledge_base/processed")
    index_dir: str = os.path.join(APP_DIR, "indexes/chroma_all_MiniLM")

    chunk_size: int = 500
    chunk_overlap: int = 75
    batch_size: int = 1000

    collection_name: str = "starwars"
    embedding_model: str = "intfloat/multilingual-e5-base"

    llm_model: str = "mistral-7b"
    llm_url: str = "http://localhost:11434"


config = Config()
