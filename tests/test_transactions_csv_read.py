from unittest.mock import mock_open, patch

from transactions_csv_read import reading_csv


def test_reading_csv():
    with patch("builtins.open", mock_open(read_data="id;state;date\n650703;EXECUTED;2023-09-05T11:30:32Z")):
        assert reading_csv("") == [{"date": "2023-09-05T11:30:32Z", "id": "650703", "state": "EXECUTED"}]
