import os

from fastapi import FastAPI

from app.api.ask import ask_router
from app.config import config
from app.scripts import (
    add_secret_document,
    build_index,
    download_and_clean,
    replace_terms,
)

app = FastAPI()

app.include_router(ask_router)


def init_app():
    if not os.path.exists(config.raw_dir):
        download_and_clean.main()
    if not os.path.exists(config.processed_dir):
        replace_terms.main()
    if not os.path.exists(config.index_dir):
        build_index.main()
        add_secret_document.main()


def main():
    print("=== Запуск приложения... ===")
    init_app()
    print("=== Приложение запущено! ===")
    import uvicorn

    print("=== Запуск сервера FastAPI... ===")
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
