from bank_read_file import process_bank_operations, search_transaction


def test_search_transaction(fixtest_search_transaction):
    assert search_transaction(fixtest_search_transaction, "пере") == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "description": "Перевод организации",
        }
    ]


def test_process_bank_operations(fixtest_process_bank_operations):
    assert process_bank_operations(fixtest_process_bank_operations, ["Открытие вклада", "Перевод организации"]) == {
        "Перевод организации": 1,
        "Открытие вклада": 1,
    }
