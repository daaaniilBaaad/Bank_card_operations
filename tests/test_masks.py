import pytest
from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number():
    expected = "1234 12** **** 1234"
    result = get_mask_card_number("1234123412341234")
    assert expected == result

def test_get_mask_card_number_error():
    expected = "Введен неверный номер карты!"
    result = get_mask_card_number("123412341234123")
    assert expected == result

def test_get_mask_account():
    expected = "**3456"
    result = get_mask_account("123456")
    assert expected == result
