from typing import List, Dict, Optional


def filter_by_state(data: List[Dict], state: Optional[str] = "EXECUTED") -> List[Dict]:
    """Функция, которая принимает список словарей и опционально значение ключа 'state'.
    Возвращает новый список словарей, у которых ключ соответствует указанному значению
    """
    return [item for item in data if item.get("state") == state]

