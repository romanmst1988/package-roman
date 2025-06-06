import pytest

from src.masks import get_mask_card_number


@pytest.mark.parametrize(
    "input_card, expected",
    [
        ("", ""),
        ("1", "1"),
        ("1234", "1234"),
        ("123456", "1234 56"),
        ("1234567", "1234 56*"),
        ("12345678", "1234 56**"),
    ],
)
def test_get_mask_card_number(input_card: str, expected: str) -> None:
    assert get_mask_card_number(input_card) == expected


@pytest.mark.parametrize(
    "input_card",
    [
        "   ",
        "--",
        "test",
        "####",
        "\t\n",
        "xxxxxxxxxxxxxxxx",
    ],
)
def test_incorrect_input(input_card: str) -> None:
    cleaned_input = input_card.strip()
    result = get_mask_card_number(cleaned_input)
    cleaned_input_no_spaces = cleaned_input.replace(" ", "")

    if len(cleaned_input_no_spaces) == 0:
        expected_masked = ""
    else:
        # Создаем список для маскировки
        card_list = list(cleaned_input_no_spaces)
        for i in range(6, 12):
            if i < len(card_list):
                card_list[i] = "*"
        masked_str = "".join(card_list)
        # Форматируем по группам по 4
        expected_masked = " ".join(masked_str[i : i + 4] for i in range(0, len(masked_str), 4))
    assert result == expected_masked


def test_empty_string() -> None:
    assert get_mask_card_number("") == ""
    assert get_mask_card_number("####") == "####"
    assert get_mask_card_number("test") == "test"
    assert get_mask_card_number("test") == "test"


def test_get_mask_card_number_len() -> None:
    assert get_mask_card_number("1234567812345678") == "1234 56** **** 5678"


def get_mask_account_valid(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    cleaned_number = account_number.replace("A-", "").replace("-B", "")
    account_mask = "**" + cleaned_number[-4:]
    if account_number == "" or len(cleaned_number) < 16:
        return "Некорректный ввод"
    return account_mask


@pytest.fixture
def account_numbers() -> list:
    return [
        "73654108430135874305",
        "7365 4108 4301 3587 4366",
        "7365-4108-4301-3587-4377",
        "A-73654108430135874305-B",
        "736541084374305",
        "",
        "ABC",
        "QWERTY",
        "+/-/*",
    ]


# Тестирование функции
@pytest.mark.parametrize(
    "index,mask",
    [
        (0, "**4305"),
        (1, "**4366"),
        (2, "**4377"),
        (3, "**4305"),
        (4, "Некорректный ввод"),
        (5, "Некорректный ввод"),
        (6, "Некорректный ввод"),
        (7, "Некорректный ввод"),
        (6, "Некорректный ввод"),
    ],
)
def test_get_mask_account(account_numbers: str, index: int, mask: str) -> None:
    account = account_numbers[index]
    assert get_mask_account_valid(account) == mask
