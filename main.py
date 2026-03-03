import argparse
import json
import logging


def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        filename="app.log",
        encoding="utf-8",
        format="%(asctime)s | %(name)s | %(levelname)s | %(message)s"
    )
    return logging.getLogger(__name__)


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


def load_config(path="config.json"):
    with open(path, "r", encoding="utf-8") as my_file:
        config = json.load(my_file)
    return config


def main():
    args = setup_args()
    logger = setup_logger()
    logger.info(f"Запуск скрипта с аргументами: {args}")


if __name__ == "__main__":
    main()