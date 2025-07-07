import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions):
    # Добавляем тестовые данные с разными валютами
    test_transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "amount": "9824.07",
            "currency_code": "USD",
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "amount": "67314.70",
            "currency_code": "RUB",
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        }
    ]

    # Тестируем USD
    usd_transactions = list(filter_by_currency(test_transactions, "USD"))
    assert len(usd_transactions) == 1
    assert usd_transactions[0]["id"] == 939719570

    # Тестируем RUB
    rub_transactions = list(filter_by_currency(test_transactions, "RUB"))
    assert len(rub_transactions) == 1
    assert rub_transactions[0]["id"] == 594226727

    # Тестируем несуществующую валюту
    assert len(list(filter_by_currency(test_transactions, "EUR"))) == 0


def test_transaction_descriptions(transactions):
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == ""
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"


def test_card_number_generator():
    _generator = card_number_generator(1, 3)
    assert next(_generator) == "0000 0000 0000 0001"
    assert next(_generator) == "0000 0000 0000 0002"
    assert next(_generator) == "0000 0000 0000 0003"
    with pytest.raises(StopIteration):
        next(_generator)
