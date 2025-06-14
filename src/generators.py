from typing import Generator

_opers = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "руб",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "eur",
                "code": "EUR"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    }
]


def filter_by_currency(operations: list[dict], currency: str) -> Generator:
    """
    Функция, которая принимает список транзакций, и возвращает генератор выдающий списки транзакций по валюте
    """
    for operation in operations:
        if operation["operationAmount"]["currency"]["code"] == currency:
            yield operation


def transaction_descriptions(transactions_list: list) -> Generator[str]:
    """Функция, которая принимает список транзакций, и возвращает описание каждой операции."""
    for transaction in transactions_list:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Generator:
    """Функция генератор, которая выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for i in range(start, stop + 1):
        card_number = []
        num = str(i).zfill(16)
        for j in range(0, 16, 4):
            card_number.append(num[j : j + 4])
        yield " ".join(card_number)

# a = card_number_generator(1, 5)
# # print(type(a))
# for i in a:
#     print(i)
#
# # print(next(a))

# b = filter_by_currency(_opers, "EUR")
# for i in b:
#     print(i)
