import pytest
import sys
import unittest
from pathlib import Path
from unittest.mock import Mock, patch
from typing import List, Dict, Any
from src.utils import process_bank_operations, process_bank_search, read_json_file

# Добавляем путь к src в PYTHONPATH
sys.path.append(str(Path(__file__).parent.parent))


class TestLoadTransactions(unittest.TestCase):

    @patch("os.path.isfile", return_value=False)
    def test_file_not_exists(self, mock_isfile: Mock) -> None:
        """Файл не существует - возвращаем []"""
        result = read_json_file("non_existent.json")
        self.assertEqual(result, [])

    @patch("os.path.isfile", return_value=True)
    def test_data_is_not_list(self, mock_isfile: Mock) -> None:
        """Данные не список - возвращаем []"""
        mock_file = Mock()
        mock_file.read = Mock(return_value='{"key": "value"}')
        # Настраиваем поддержку контекстного менеджера
        mock_file.__enter__ = Mock(return_value=mock_file)
        mock_file.__exit__ = Mock(return_value=None)
        with patch("builtins.open", return_value=mock_file):
            result = read_json_file("not_a_list.json")
            self.assertEqual(result, [])

    @patch("os.path.isfile", return_value=True)
    def test_invalid_json(self, mock_isfile: Mock) -> None:
        """Невалидный JSON - возвращаем []"""
        mock_file = Mock()
        mock_file.read = Mock(return_value="{invalid json}")
        # Настраиваем поддержку контекстного менеджера
        mock_file.__enter__ = Mock(return_value=mock_file)
        mock_file.__exit__ = Mock(return_value=None)
        with patch("builtins.open", return_value=mock_file):
            result = read_json_file("invalid.json")
            self.assertEqual(result, [])

    @patch("os.path.isfile", return_value=True)
    def test_valid_case(self, mock_isfile: Mock) -> None:
        """Корректные данные - возвращаем список транзакций"""
        mock_file = Mock()
        mock_file.read = Mock(return_value='[{"id": 1, "amount": 100}]')
        # Настраиваем поддержку контекстного менеджера
        mock_file.__enter__ = Mock(return_value=mock_file)
        mock_file.__exit__ = Mock(return_value=None)
        with patch("builtins.open", return_value=mock_file):
            result = read_json_file("valid.json")
            self.assertEqual(result, [{"id": 1, "amount": 100}])


@pytest.fixture
def transactions() -> List[Dict[str, Any]]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "amount": "9824.07",
            "currency_name": "USD",
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
            "currency_name": "руб.",
            "currency_code": "RUB",
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_process_bank_search(transactions: List[Dict[str, Any]]) -> None:
    assert process_bank_search(transactions, "Перевод организации") == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "amount": "9824.07",
            "currency_name": "USD",
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
            "currency_name": "руб.",
            "currency_code": "RUB",
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_process_bank_operations(transactions: List[Dict[str, Any]]) -> None:
    assert process_bank_operations(transactions, ["Перевод организации", "Перевод со счета на счет"]) == {
        "Перевод организации": 2,
        "Перевод со счета на счет": 2,
    }
