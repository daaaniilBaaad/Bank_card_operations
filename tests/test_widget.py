from src.widget import mask_account_card, get_date
import pytest

@pytest.mark.parametrize(
    "entry_value, expected", [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Platinum 7365410843013587", "VisaPlatinum 7365 41** **** 3587")
    ]
)

def test_mask_account_card(entry_value, expected):
    result = mask_account_card(entry_value)
    assert expected == result


# def test_mask_account_card_error(capsys):
#     result = mask_account_card("Visa Platinum")
#     captured_output = capsys.readouterr()
#     print(captured_output)

def test_mask_account_card_error():
    result = mask_account_card("Visa Platinum")
    expected = "VisaPlatinum Введен неверный номер карты!"
    assert expected == result

def test_get_date():
    assert get_date("2025-06-08T18:14:18.671407") == "08.06.2025"