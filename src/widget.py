import datetime
from typing import Union

from src.masks import get_mask_account, get_mask_card_number


# def mask_account_card(type_and_number: Union[str]) -> Union[str]:
#     """Функция, которая принимает тип и номер карты(счета) маскируя номер."""
#     account_type = ""
#     account_number = ""
#     digit_count = 0
#     for el in type_and_number:
#         if el.isalpha():
#             account_type += el
#         elif el.isdigit():
#             account_number += el
#             digit_count += 1
#     if digit_count > 16:
#         return f"{account_type} {get_mask_account(account_number)}"
#     else:
#         return f"{account_type} {get_mask_card_number(account_number)}"


def mask_account_card(name_card: Union[str, float, None]) -> str:
    """принимает карту/счет, возвращает тип карты/счета и замаскированный номер карты/счета"""
    # Обработка случаев, когда name_card не строка
    if not isinstance(name_card, str):
        return "Нет данных"

    name_card = str(name_card).strip()  # На всякий случай преобразуем в строку

    if not name_card:
        return "Нет данных"

    if "счет" in name_card.lower():
        # Обработка счета
        digits = "".join([c for c in name_card if c.isdigit()])
        if len(digits) == 20:
            masked = f"**{digits[-4:]}"
            return f"счет {masked}"
        return "Некорректный номер счета"

    # Обработка карты
    digits = "".join([c for c in name_card if c.isdigit()])
    if len(digits) == 16:
        masked = f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"
        # Сохраняем текст перед номером (название карты)
        text_part = "".join([c for c in name_card if not c.isdigit()]).strip()
        return f"{text_part} {masked}"

    return "Некорректные данные карты"


def get_date(time_card: str) -> str:
    """принимает системную дату/время, возвращает дату в формате ДД.ММ.ГГГГ"""
    return time_card[8:10] + "." + time_card[5:7] + "." + time_card[:4]

# print(mask_account_card("Счет 73654108430135874305"))
# print(mask_account_card("Visa Platinum 7365410843013587"))
# print(mask_account_card("Visa Platinum"))