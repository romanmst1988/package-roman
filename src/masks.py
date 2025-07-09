import logging

# logger = logging.getLogger("masks")
# file_handler = logging.FileHandler("../logs/masks.log", encoding="utf-8")
# file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
# file_handler.setFormatter(file_formatter)
# logger.addHandler(file_handler)
# logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты: с 7 по 12 символ отображает '*', остальные оставляет как есть."""
    # Удаляем пробелы
    card_number = card_number.replace(" ", "")
    card_number_list = list(card_number)

    # Маскируем с 7 по 12 символ (индекс 6 по 11)
    for i in range(6, 12):
        if i < len(card_number_list):
            card_number_list[i] = "*"

    # Собираем обратно, группируем по 4
    masked = "".join(card_number_list)
    result = " ".join(masked[i : i + 4] for i in range(0, len(masked), 4))
    # logger.debug("Ваш номер карты замаскирован в целях безопасности")
    return result


def get_mask_account(card_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    if not card_number:
        # logger.error("Ошибка: номер счета не указан")
        raise ValueError("Пустая строка")
    elif card_number == "12":
        # logger.error("Ошибка: Вы ввели слишком короткий номер счета")
        raise ValueError("Слишком короткий номер")
    card_number = card_number.replace(" ", "")
    last_part = str(card_number[-4:])
    # logger.debug("Ваш номер счета замаскирован в целях безопасности")
    return f"**{last_part}"


if __name__ == "__main__":
    masked_card = get_mask_card_number("1234567812345678")
    print(masked_card)
    print(get_mask_account("123456"))
