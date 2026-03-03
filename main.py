import argparse
import json
import os

def setup_args():
    parser = argparse.ArgumentParser(
        description="Скрипт, для обработки каталогов."
    )

    parser.add_argument(
        "-p", "--path",
        type=str,
        required=True,
        help="Обязательный путь к основному каталогу."
    )

    parser.add_argument(
        "-d", "--dry-run",
        action="store_true",
        help="Режим 'холостого' запуска без внесения изменений"
    )

    return parser.parse_args()


def load_config(path=os.path.abspath("config.json")):
    with open(path, "r", encoding="utf-8") as my_file:
        config = json.load(my_file)
    return config



def main():
    args = setup_args()
    print(args)


if __name__ == "__main__":
    main()