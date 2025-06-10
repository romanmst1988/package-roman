import pytest

# Фикстура с тестовыми случаями для get_mask_card_number для test_masks
@pytest.fixture
def mask_card_number_cases() -> list:
    return [
        ("", ""),
        ("1", "1"),
        ("1234", "1234"),
        ("123456", "1234 56"),
        ("1234567", "1234 56*"),
        ("12345678", "1234 56**"),
    ]

# Фикстура с некорректными входными данными для test_masks
@pytest.fixture
def incorrect_input_cases() -> list:
    return [
        "   ",
        "--",
        "test",
        "####",
        "\t\n",
        "xxxxxxxxxxxxxxxx",
    ]

# Фикстура с различными тестовыми строками для проверки маскировки для test_masks
@pytest.fixture
def diverse_inputs() -> list:
    return [
        "",
        "####",
        "test",
        "1234567812345678",
    ]

# Фикстура с номерами счетов для функции get_mask_account_valid для test_masks
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

# Фикстура, предоставляющая невалидные входные данные для get_mask_account для test_masks
@pytest.fixture(params=["", "12"])
def invalid_account_input(request) -> str:
    return request.param

# Фикстура с исходным списком данных для test_processing
@pytest.fixture
def sample_data() -> list:
    return [
        {"id": 1, "amount": 100, "state": "EXECUTED"},
        {"id": 2, "amount": 200, "state": "PENDING"},
        {"id": 3, "amount": 300, "state": "CANCELLED"},
        {"id": 4, "amount": 400, "state": "EXECUTED"},
        {"id": 5, "amount": 500, "state": "PENDING"},
    ]

# Фикстура с исходными данными для test_processing
@pytest.fixture
def sample_data_1() -> list:
    return [
        {"id": 1, "date": "2023-10-01T12:00:00"},
        {"id": 2, "date": "2023-09-15T09:30:00"},
        {"id": 3, "date": "2023-10-05T18:45:00"},
        {"id": 4, "date": "2023-09-15T09:30:00"},
        {"id": 5, "date": "2022-12-31T23:59:59"},
    ]

# Фикстура для корректных строк с картами и счетами для test_widget
@pytest.fixture
def valid_card_and_account() -> list:
    return [
        ("Visa Platinum 7000792289606361", "Visa Platinum  7000 79** **** 6361"),
        ("MasterCard Gold 1234567890123456", "MasterCard Gold  1234 56** **** 3456"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Мой счет 09876543210987654321", "Счет **4321"),
    ]

# Фикстура для типов (карта или счет) для test_widget
@pytest.fixture
def type_samples() -> list:
    return [
        ("Visa 1234567890123456", "карта"),
        ("Счет 12345678901234567890", "счет"),
    ]

# Фикстура для некорректных входных данных для mask_account_card для test_widget
@pytest.fixture
def invalid_mask_inputs() -> list:
    return [
        "",
        "Visa",
    ]

# Фикстура для правильных дат для test_widget
@pytest.fixture
def valid_dates() -> list:
    return [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("1999-12-31T23:59:59.999999", "31.12.1999"),
        ("2020-01-01T00:00:00", "01.01.2020"),
    ]

# Фикстура для граничных и необычных дат для test_widget
@pytest.fixture
def edge_case_dates() -> list:
    return [
        ("0000-00-00T00:00:00", "00.00.0000"),
        ("9999-12-31T23:59:59", "31.12.9999"),
    ]