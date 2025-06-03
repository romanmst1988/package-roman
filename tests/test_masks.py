import pytest
from src.masks import get_mask_card_number, get_mask_account


def get_mask_card_number(card_number: str) -> str:
    # Проверка на пустую строку или строку без цифр
    if not card_number or not any(char.isdigit() for char in card_number):
        raise ValueError("Входная строка должна содержать цифры")

    # Удаляем все пробелы
    cleaned_number = card_number.replace(" ", "")

    # Проверка, что остались только цифры
    if not cleaned_number.isdigit():
        raise ValueError("Некорректный номер карты: должны быть только цифры")

    # Проверка длины номера
    length = len(cleaned_number)
    if length < 12 or length > 20:
        raise ValueError("Некорректная длина номера карты")

    # Формируем строку с пробелами по 4 символа
    masked_card_number = " ".join(
        cleaned_number[i: i + 4] for i in range(0, length, 4)
    )

    # Преобразуем в список для маскировки
    masked_list = list(masked_card_number)

    # Маскируем символы с позиций 7 по 13 (учитывая пробелы)
    for i in range(len(masked_list)):
        if 7 <= i <= 13 and masked_list[i] != " ":
            masked_list[i] = "*"

    return "".join(masked_list)


# Тест с номерами, где есть лишние пробелы внутри
@pytest.mark.parametrize("input_str, expected_output", [
    (" 1234   5678 9012   3456 ", "1234 56** **** 3456"),
])
def test_input_with_extra_spaces(input_str, expected_output):
    result = get_mask_card_number(input_str)
    assert result == expected_output

# 3. Проверка обработки входных строк без номера карты или некорректных данных
@pytest.mark.parametrize("invalid_input", [
    "",             # пустая строка
    "     ",        # только пробелы
    "abc def ghi",  # буквы вместо цифр
    "12ab34",       # смешанные символы
])
def test_invalid_inputs(invalid_input):
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_input)

# Также проверка на длину менее минимальной и более максимальной
@pytest.mark.parametrize("invalid_input, error_msg", [
    ("12345", "Некорректная длина номера карты"),          # меньше минимальной длины (12)
    ("1" * 21, "Некорректная длина номера карты"),       # больше максимальной длины (20)
])
def test_length_constraints(invalid_input, error_msg):
    with pytest.raises(ValueError) as e:
        get_mask_card_number(invalid_input)
    assert error_msg in str(e.value)


# def get_mask_account(account_number: str) -> str:
#     """Функция принимает на вход номер счета и возвращает его маску."""
#     cleaned_number = account_number.replace("A-", "").replace("-B", "")
#     account_mask = "**" + cleaned_number[-4:]
#     if account_number == "" or len(cleaned_number) < 16:
#         return "Некорректный ввод"
#     return account_mask
#
#
# @pytest.fixture
# def account_numbers():
#     return [
#         "73654108430135874305",
#         "7365 4108 4301 3587 4366",
#         "7365-4108-4301-3587-4377",
#         "A-73654108430135874305-B",
#         "736541084374305",
#         "",
#         "ABC",
#         "QWERTY",
#         "+/-/*"
#     ]
#
# # Тестирование функции get_mask_account
# @pytest.mark.parametrize(
#     "index,mask",
#     [
#         (0, "**4305"),
#         (1, "**4366"),
#         (2, "**4377"),
#         (3, "**4305"),
#         (4, "Некорректный ввод"),
#         (5, "Некорректный ввод"),
#         (6, "Некорректный ввод"),
#         (7, "Некорректный ввод"),
#         (6, "Некорректный ввод")
#     ],
# )
# def test_get_mask_account(account_numbers, index, mask):
#     account = account_numbers[index]
#     assert get_mask_account(account) == mask
