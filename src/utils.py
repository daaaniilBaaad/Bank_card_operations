import json
import logging
import os
import re
from collections import Counter
from pathlib import Path
from typing import List, Union

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

os.makedirs("logs", exist_ok=True)
fh = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
logger.handlers.clear()
logger.addHandler(fh)
logger.propagate = False


def read_json_file(file_path: Union[str, Path]) -> List[dict]:
    try:
        logger.info(f"Чтение файла: {file_path}")
        print(f"DEBUG: Попытка открыть файл: {file_path}")  # Для проверки в консоли
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Успешно прочитано {len(data)} элементов из файла {file_path}")
                return data
            else:
                logger.warning(f"Файл {file_path} не содержит список, возвращается пустой список")
                return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}", exc_info=True)
        return []
    except json.JSONDecodeError:
        logger.error(f"Некорректный JSON в файле: {file_path}", exc_info=True)
        return []
    except Exception as e:
        logger.error(f"Неожиданная ошибка при чтении файла {file_path}: {str(e)}", exc_info=True)
        return []


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """функция фильтрует список операций по заданным словам"""
    result = []
    re_pattern = re.compile(search, re.IGNORECASE)
    for operation in data:
        if re_pattern.search(str(operation.get("description", ""))):
            result.append(operation)
    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция принимающая список словарей с данными об операциях и список категорий
    и возвращает словарь с ключами - названия категорий, а значения - кол-во операций
    """
    count_categories = []
    for operation in data:
        if operation.get("description", "") in categories:
            count_categories.append(operation.get("description", ""))
    return dict(Counter(count_categories))


if __name__ == "__main__":
    result = read_json_file("no_such_file.json")
    print(f"Result: {result}")
