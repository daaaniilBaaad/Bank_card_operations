import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number()-> None:
    expected = "1234 12** **** 1234"
    result = get_mask_card_number("1234123412341234")
    assert expected == result

def test_get_mask_card_number_error()-> None:
    expected = "Введен неверный номер карты!"
    result = get_mask_card_number("123412341234123")
    assert expected == result

def test_get_mask_account()-> None:
    expected = "**3456"
    result = get_mask_account("123456")
    assert expected == result

