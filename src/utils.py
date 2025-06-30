import json
import os
from typing import Any, Dict, List


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    if not os.path.isfile(file_path):
        return []  # Если файл не существует, вернуть пустой список

    with open(file_path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)  # Попытка загрузить данные из файла
            if isinstance(data, list):  # Проверка, является ли загруженные данные списком
                return data
            return []  # Если данные не список, вернуть пустой список
        except json.JSONDecodeError:
            return []  # Если ошибка при декодировании JSON, вернуть пустой список
