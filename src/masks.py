import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)


formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)


logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция получает номер карты и выводит первые 6 и последние 4 цифры, остальные заменяет '*'"""
    logger.info("Обработка номера карты (первые 6, последние 4 цифры): %s...%s", card_number[:6], card_number[-4:])

    card_number = card_number.replace(" ", "")
    if len(card_number) != 16:
        logger.error("Неверная длина номера карты: %s цифр", len(card_number))
        return "Введен неверный номер карты!"

    result = []
    for i, number in enumerate(card_number):
        if 6 <= i < 12:
            result.append("*")
        else:
            result.append(number)

    masked_card = "".join(result)
    masked_card_result_with_space = " ".join([masked_card[i : i + 4] for i in range(0, len(masked_card), 4)])

    logger.info("Успешно замаскирован номер карты: %s", masked_card_result_with_space)
    return masked_card_result_with_space


def get_mask_account(card_number: str) -> str:
    """Функция получает номер счета и выводит 2 '*' и 4 последние цифры"""
    logger.info("Обработка номера счета (последние 4 цифры): ...%s", card_number[-4:])

    card_number = card_number.replace(" ", "")
    if len(card_number) != 20 or not card_number.isdigit():
        logger.error("Неверный номер счета: длина=%s, все цифры=%s", len(card_number), card_number.isdigit())
        return "Введите корректный номер карты"

    masked_account = f"**{card_number[-4:]}"
    logger.info("Успешно замаскирован номер счета: %s", masked_account)
    return masked_account


if __name__ == "__main__":
    print(get_mask_card_number("1234567890123456"))  # Ожидаемый вывод: 123456******3456 (с пробелами)
    print(get_mask_account("12345678901234567890"))  # Ожидаемый вывод: **7890
    print(get_mask_card_number("123456789012345"))  # Ожидаемый вывод: Введен неверный номер карты!
    print(get_mask_account("1234567890123456789a"))  # Ожидаемый вывод: Введите корректный номер карты
