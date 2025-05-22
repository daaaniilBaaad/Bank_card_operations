from src.masks import get_mask_card_number, get_mask_account
from typing import Union
import datetime


def mask_account_card(type_and_number: Union[str]) -> Union[str]:
    """Функция, которая принимает тип и номер карты(счета) маскируя номер."""
    account_type = ""
    account_number = ""
    digit_count = 0
    for el in type_and_number:
        if el.isalpha():
            account_type += el
        elif el.isdigit():
            account_number += el
            digit_count += 1
    if digit_count > 16:
        return f"{account_type} {get_mask_account(account_number)}"
    else:
        return f"{account_type} {get_mask_card_number(account_number)}"
