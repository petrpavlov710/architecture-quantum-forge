import os
import re

from app.config import config
from app.scripts.terms_map import terms_map


def main():
    os.makedirs(config.processed_dir, exist_ok=True)

    for fn in os.listdir(config.raw_dir):
        raw_path = os.path.join(config.raw_dir, fn)
        proc_path = os.path.join(config.processed_dir, fn)

        text = open(raw_path, encoding="utf-8").read()
        text = text.lower()

        for src, dst in terms_map.items():
            pattern = re.compile(re.escape(src.lower()))
            text = pattern.sub(dst.lower(), text)

        with open(proc_path, "w", encoding="utf-8") as out:
            out.write(text)

        print(f"[OK] {fn} → обработка завершена.")


if __name__ == "__main__":
    main()
    print("Все файлы успешно обработаны.")
