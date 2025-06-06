import pytest

from src.processing import filter_by_state, sort_by_date


# Фикстура с исходным списком данных
@pytest.fixture
def sample_data() -> list:
    return [
        {"id": 1, "amount": 100, "state": "EXECUTED"},
        {"id": 2, "amount": 200, "state": "PENDING"},
        {"id": 3, "amount": 300, "state": "CANCELLED"},
        {"id": 4, "amount": 400, "state": "EXECUTED"},
        {"id": 5, "amount": 500, "state": "PENDING"},
    ]


# Параметризация для различных статусов
@pytest.mark.parametrize(
    "status, expected_ids",
    [
        ("EXECUTED", [1, 4]),
        ("PENDING", [2, 5]),
        ("CANCELLED", [3]),
    ],
)
def test_filter_by_state_correctness(sample_data: list, status: str, expected_ids: list) -> None:
    result = filter_by_state(sample_data, status)
    result_ids = [item["id"] for item in result]
    assert result_ids == expected_ids


# Тест на случай отсутствия элементов с заданным статусом
def test_filter_by_state_no_matches(sample_data: list) -> None:
    # Статус отсутствует в данных
    result = filter_by_state(sample_data, "COMPLETED")
    assert result == []


# Тест на работу функции без указания статуса
def test_filter_by_state_default(sample_data: list) -> None:
    # По умолчанию ищем 'EXECUTED'
    result = filter_by_state(sample_data)
    expected_ids = [1, 4]
    result_ids = [item["id"] for item in result]
    assert result_ids == expected_ids


# Тест на пустой список входных данных
def test_filter_by_state_empty_list() -> None:
    empty_list: list[dict] = []
    result = filter_by_state(empty_list, "EXECUTED")
    assert result == []


# Тест на список с одним элементом
def test_filter_by_state_single_element() -> None:
    data = [{"id": 10, "amount": 1000, "state": "PENDING"}]

    # Проверка с совпадающим статусом
    result = filter_by_state(data, "PENDING")
    assert result == data

    # Проверка с несовпадающим статусом
    result2 = filter_by_state(data, "EXECUTED")
    assert result2 == []


# Фикстура с исходными данными
@pytest.fixture
def sample_data_1() -> list:
    return [
        {"id": 1, "date": "2023-10-01T12:00:00"},
        {"id": 2, "date": "2023-09-15T09:30:00"},
        {"id": 3, "date": "2023-10-05T18:45:00"},
        {"id": 4, "date": "2023-09-15T09:30:00"},
        {"id": 5, "date": "2022-12-31T23:59:59"},
    ]


@pytest.mark.parametrize(
    "reverse_flag, expected_order_ids",
    [
        (False, [5, 2, 4, 1, 3]),
        (True, [3, 1, 2, 4, 5]),
    ],
)
def test_sort_by_date_order(sample_data_1: list[dict], reverse_flag: bool, expected_order_ids: list) -> None:
    sorted_list = sort_by_date(sample_data_1, reverse=reverse_flag)
    result_ids = [item["id"] for item in sorted_list]
    assert result_ids == expected_order_ids


# Тест на одинаковые даты
def test_sort_with_equal_dates() -> None:
    data = [
        {"id": 1, "date": "2023-10-01T12:00:00"},
        {"id": 2, "date": "2023-10-01T12:00:00"},
        {"id": 3, "date": "2023-09-15T09:30:00"},
        {"id": 4, "date": "2023-10-05T18:45:00"},
    ]
    sorted_data = sort_by_date(data)
    sorted_ids = [item["id"] for item in sorted_data]
    assert sorted_ids == [3, 1, 2, 4]
