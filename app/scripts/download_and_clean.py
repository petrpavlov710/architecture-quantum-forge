import os
import re
from typing import Tuple

import requests
from bs4 import BeautifulSoup
from slugify import slugify

from app.config import config


def download(url: str) -> None:
    response = requests.get(url)
    response.raise_for_status()
    title, text = clean(response.text)
    fn = f"{slugify(title)}.txt"
    file_path = os.path.join(config.raw_dir, fn)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)
    print(f"[OK] Downloaded {fn} ")


def clean(content: str) -> Tuple[str, str]:
    soup = BeautifulSoup(content, "html.parser")
    content_div = soup.find("div", id="mw-content-text")
    text = content_div.get_text(separator="\n")
    text = re.sub(r"\n+", " ", text)
    text = re.sub(r"\[\d+\]", "", text)
    text = re.sub(r"\{\{[^}]+\}\}", "", text)
    text = text.strip()

    title = soup.find("h1", id="firstHeading").get_text()
    return title, text


def main():
    pass
    os.makedirs(config.raw_dir, exist_ok=True)

    with open(f"{config.knowledge_dir}/urls.txt") as url_file:
        urls = [line.strip() for line in url_file if line.strip()]

    for url in urls:
        try:
            download(url)
        except Exception as e:
            print(f"[ERROR] {url}: {e}")
            continue


if __name__ == "__main__":
    main()
