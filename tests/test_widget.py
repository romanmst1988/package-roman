import pytest

from src.widget import get_date, mask_account_card


# 1. Тесты для проверки правильного распознавания типа и применения маскировки
@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum  7000 79** **** 6361"),
        ("MasterCard Gold 1234567890123456", "MasterCard Gold  1234 56** **** 3456"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Мой счет 09876543210987654321", "Счет **4321"),
    ],
)
def test_masking_correctness(input_str: str, expected_output: str) -> None:
    result = mask_account_card(input_str)
    assert result == expected_output


# 2. Проверка, что функция распознает тип (карта или счет) и применяет соответствующую маску
@pytest.mark.parametrize(
    "input_str, expected_type",
    [
        ("Visa 1234567890123456", "карта"),
        ("Счет 12345678901234567890", "счет"),
    ],
)
def test_type_recognition(input_str: str, expected_type: str) -> None:
    result = mask_account_card(input_str)
    if expected_type == "карта":
        # Проверяем наличие маскировки и названия карты
        assert "****" in result
        assert any(name in result for name in ["Visa", "MasterCard"])
    else:
        # Проверяем, что результат начинается с 'Счет' и содержит маску
        assert result.startswith("Счет")
        assert "**" in result


# 3. Тесты на некорректные входные данные
@pytest.mark.parametrize(
    "bad_input",
    [
        "",
        "Visa",  # без номера карты
    ],
)
def test_mask_account_card_invalid_inputs(bad_input: str) -> None:
    # Ожидаем, что функция выбросит исключение или обработает ошибку
    with pytest.raises(ValueError):
        mask_account_card(bad_input)


# Тестирование правильности преобразования даты
@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("1999-12-31T23:59:59.999999", "31.12.1999"),
        ("2020-01-01T00:00:00", "01.01.2020"),
    ],
)
def test_get_date_correctness_valid(input_str: str, expected_output: str) -> None:
    result = get_date(input_str)
    assert result == expected_output


# Тестирование обработки различных форматов и граничных случаев
@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        ("0000-00-00T00:00:00", "00.00.0000"),  # граничный случай с нулями
        ("9999-12-31T23:59:59", "31.12.9999"),  # последний день года
        #     2024-03-11T02:26:18.671407
    ],
)
def test_get_date_edge_cases(input_str: str, expected_output: str) -> None:
    result = get_date(input_str)
    assert result == expected_output


@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("1999-12-31T23:59:59.999999", "31.12.1999"),
    ],
)
def test_get_date_correctness(input_str: str, expected_output: str) -> None:
    assert get_date(input_str) == expected_output


@pytest.mark.parametrize(
    "bad_input",
    [
        "",  # пустая строка
        "2024/03/11T02:26:18",  # неправильный формат разделителя
        "20240311T02:26:18",  # без дефисов
    ],
)
def test_get_date_invalid_inputs(bad_input: str) -> None:
    with pytest.raises(ValueError):
        get_date(bad_input)
