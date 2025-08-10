import os
import time

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

from app.config import config
from app.engine import get_engine


def chunk_docs():
    print("=== Разделение документов на части (chunks) ===")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.chunk_size, chunk_overlap=config.chunk_overlap
    )

    all_chunks = []
    for fn in sorted(os.listdir(config.processed_dir)):
        path = os.path.join(config.processed_dir, fn)

        file_chunks = splitter.split_documents(TextLoader(path).load())
        for number, chunk in enumerate(file_chunks):
            chunk.metadata["source"] = fn
            chunk.metadata["chunk"] = number
        all_chunks.extend(file_chunks)

    print(f"Всего частей: {len(all_chunks)}")
    return all_chunks


def build_and_save_embeddings(chunks):
    print("=== Загрузка эмбеддинг-модели ===")
    db = get_engine()

    for i in range(0, len(chunks), config.batch_size):
        batch = chunks[i : i + config.batch_size]
        print(f"Добавляем части {i}–{i + len(batch)} из {len(chunks)}...")
        db.add_documents(batch)

    print(f"Индекс сохранён в: {config.index_dir}")


def main():
    os.makedirs(config.index_dir, exist_ok=True)
    start_time = time.time()
    chunks = chunk_docs()
    build_and_save_embeddings(chunks)
    delta_time = time.time() - start_time
    print(f"Сборка индекса завершена за {delta_time:.2f} секунд.")


if __name__ == "__main__":
    main()
