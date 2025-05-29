from typing import Dict, List, Optional


def filter_by_state(data: List[Dict], state: Optional[str] = "EXECUTED") -> List[Dict]:
    """Функция, которая принимает список словарей и опционально значение ключа 'state'.
    Возвращает новый список словарей, у которых ключ соответствует указанному значению
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(info_list: List[Dict], reverse: bool = True) -> List[Dict]:
    """Функция, которая принимает список словарей и параметр, задающий порядок сортировки.
    Возвращает новый список, отсортированный по дате
    """
    return sorted(info_list, key=lambda x: x["date"], reverse=True)