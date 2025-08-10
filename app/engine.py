from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from app.config import config


def get_engine():
    db = Chroma(
        collection_name=config.collection_name,
        embedding_function=HuggingFaceEmbeddings(model_name=config.embedding_model),
        persist_directory=config.index_dir,
    )
    return db
