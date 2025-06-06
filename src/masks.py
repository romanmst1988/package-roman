
# Запускаем функцию с аргументом

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
    result = " ".join(masked[i:i + 4] for i in range(0, len(masked), 4))
    return result

def get_mask_account(card_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""

    card_number = card_number.replace(" ", "")
    last_part = str(card_number[-4:])
    return f"**{last_part}"

if __name__ == "__main__":
    masked_card = get_mask_card_number("1234567812345678")
    print(masked_card)
    print(get_mask_account("123456"))


# def mask_account_card():
#     return None
#
#
# def mask_account():
#     return None