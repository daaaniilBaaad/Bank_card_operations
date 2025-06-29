import unittest
from unittest.mock import patch, Mock
import sys
from pathlib import Path
from typing import List, Dict, Any

# Добавляем путь к src в PYTHONPATH
sys.path.append(str(Path(__file__).parent.parent))

from src.utils import load_transactions


class TestLoadTransactions(unittest.TestCase):

    @patch("os.path.isfile", return_value=False)
    def test_file_not_exists(self, mock_isfile):
        """Файл не существует - возвращаем []"""
        result = load_transactions("non_existent.json")
        self.assertEqual(result, [])

    @patch("os.path.isfile", return_value=True)
    def test_data_is_not_list(self, mock_isfile):
        """Данные не список - возвращаем []"""
        mock_file = Mock()
        mock_file.read = Mock(return_value='{"key": "value"}')
        # Настраиваем поддержку контекстного менеджера
        mock_file.__enter__ = Mock(return_value=mock_file)
        mock_file.__exit__ = Mock(return_value=None)
        with patch("builtins.open", return_value=mock_file):
            result = load_transactions("not_a_list.json")
            self.assertEqual(result, [])

    @patch("os.path.isfile", return_value=True)
    def test_invalid_json(self, mock_isfile):
        """Невалидный JSON - возвращаем []"""
        mock_file = Mock()
        mock_file.read = Mock(return_value="{invalid json}")
        # Настраиваем поддержку контекстного менеджера
        mock_file.__enter__ = Mock(return_value=mock_file)
        mock_file.__exit__ = Mock(return_value=None)
        with patch("builtins.open", return_value=mock_file):
            result = load_transactions("invalid.json")
            self.assertEqual(result, [])

    @patch("os.path.isfile", return_value=True)
    def test_valid_case(self, mock_isfile):
        """Корректные данные - возвращаем список транзакций"""
        mock_file = Mock()
        mock_file.read = Mock(return_value='[{"id": 1, "amount": 100}]')
        # Настраиваем поддержку контекстного менеджера
        mock_file.__enter__ = Mock(return_value=mock_file)
        mock_file.__exit__ = Mock(return_value=None)
        with patch("builtins.open", return_value=mock_file):
            result = load_transactions("valid.json")
            self.assertEqual(result, [{"id": 1, "amount": 100}])


if __name__ == "__main__":
    unittest.main()