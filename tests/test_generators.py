import pytest

from generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "currency, expected_count",
    [
        ("USD", 3),
        ("RUB", 2),
        ("EUR", 0),
    ],
)
def test_filter_by_currency(transactions_data: list, currency: str, expected_count: str) -> None:
    result = list(filter_by_currency(transactions_data, currency))
    assert len(result) == expected_count
    for transaction in result:
        assert transaction["operationAmount"]["currency"]["code"] == currency


def test_filter_by_currency_empty_list(empty_transactions_data: list) -> None:
    result = list(filter_by_currency(empty_transactions_data, "USD"))
    assert len(result) == 0


# Тест для transaction_descriptions
def test_transaction_descriptions_correct_descriptions(transactions_data: list) -> None:
    result = list(transaction_descriptions(transactions_data))
    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert result == expected_descriptions


def test_transaction_descriptions_empty_list(empty_transactions_data: list) -> None:
    result = list(transaction_descriptions(empty_transactions_data))
    assert len(result) == 0


def test_transaction_descriptions_single_transaction(transactions_data: list) -> None:
    result = list(transaction_descriptions([transactions_data[0]]))
    assert result == ["Перевод организации"]


# Тест для card_number_generator
@pytest.mark.parametrize(
    "start, count, expected_first",
    [
        (1000, 3, "0000 0000 0000 1000"),
        (1, 1, "0000 0000 0000 0001"),
        (9999999999999999, 1, "9999 9999 9999 9999"),
    ],
)
def test_card_number_generator(start: int, count: int, expected_first: int) -> None:
    generator = card_number_generator(start, count)
    assert next(generator) == expected_first
    if count > 1:
        next(generator)


@pytest.mark.parametrize(
    "start, count",
    [
        (100, 0),
    ],
)
def test_card_number_generator_zero_range(start: int, count: int) -> None:
    generator = card_number_generator(start, count)
    with pytest.raises(StopIteration):
        next(generator)
