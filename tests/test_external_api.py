import unittest
from unittest.mock import Mock, patch

from src.external_api import convert_to_rub


class TestConvertToRub(unittest.TestCase):

    def test_rub_currency_no_conversion(self) -> None:
        """Тест транзакции в RUB (конвертация не требуется)"""
        transaction = {"amount": "100.50", "currency": "RUB"}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 100.50)

    @patch("requests.get")
    @patch.dict("os.environ", {"APILAYER_KEY": "test_api_key"})
    def test_successful_conversion(self, mock_get: Mock) -> None:
        """Тест успешной конвертации"""
        # Настраиваем mock для requests.get
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json = Mock(return_value={"result": 7500.0})
        mock_get.return_value = mock_response

        transaction = {"amount": "100", "currency": "USD"}
        result = convert_to_rub(transaction)

        self.assertEqual(result, 7500.0)
        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100",
            headers={"apikey": "test_api_key"},
        )

    @patch("requests.get")
    @patch.dict("os.environ", {"APILAYER_KEY": "test_api_key"})
    def test_failed_conversion(self, mock_get: Mock) -> None:
        """Тест неудачной конвертации (возвращаем исходную сумму)"""
        # Настраиваем mock для requests.get
        mock_response = Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        transaction = {"amount": "100", "currency": "EUR"}
        result = convert_to_rub(transaction)

        self.assertEqual(result, 100.0)
        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=100",
            headers={"apikey": "test_api_key"},
        )

    @patch("requests.get")
    @patch.dict("os.environ", {"APILAYER_KEY": "test_api_key"})
    def test_invalid_api_response(self, mock_get: Mock) -> None:
        """Тест невалидного ответа API (ожидаем KeyError)"""
        # Настраиваем mock для requests.get
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json = Mock(return_value={})  # Ответ без ключа "result"
        mock_get.return_value = mock_response

        transaction = {"amount": "100", "currency": "GBP"}

        # Проверяем, что функция выбрасывает KeyError
        with self.assertRaises(KeyError):
            convert_to_rub(transaction)

        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=GBP&amount=100",
            headers={"apikey": "test_api_key"},
        )


if __name__ == "__main__":
    unittest.main()
