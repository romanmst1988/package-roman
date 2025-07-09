from unittest.mock import patch

from transactions_xlsx_read import reading_xlsx


@patch("pandas.read_excel")
def test_reading_xlsx(mock_get):
    mock_get.return_value.to_dict.return_value = [
        {"date": "2023-09-05T11:30:32Z", "id": "650703", "state": "EXECUTED"}
    ]
    assert reading_xlsx("") == [{"date": "2023-09-05T11:30:32Z", "id": "650703", "state": "EXECUTED"}]