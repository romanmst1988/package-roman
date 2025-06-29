from unittest.mock import mock_open, patch

import pytest

from src.utils import convertor_to_rubles, open_json


# Тест при верной и неверной (неполной) структуре JSON-файла
def test_open_json_correct():
    with patch("builtins.open", mock_open(read_data='{"1" : "2"}')):
        assert open_json("") == {"1": "2"}
    with patch("builtins.open", mock_open(read_data='{"1" : "2"')):
        assert open_json("") == []
    assert open_json("") == []


# Параметризированный тест при верной и неверной (неполной) структуре обрабатываемого словаря
@pytest.mark.parametrize(
    "oper_dict, result",
    (
        ({"operationAmount": {"amount": "100", "currency": {"name": "USD", "code": "USD"}}}, 7860.9512),
        ({"operationAmount": {"amount": "100", "currency": {"name": "RUB", "code": "RUB"}}}, 100.0),
        ({"operation": {"amount": "100", "currency": {"name": "RUB", "code": "RUB"}}}, 0.0),
        ({"operationAmount": {"amount": "100", "currency": {"name": "RUB", "cod": "RUB"}}}, 0.0),
        ({}, 0.0),
    ),
)
def test_convertor_to_rubles(oper_dict, result):
    need_result = convertor_to_rubles(oper_dict)
    assert need_result == result