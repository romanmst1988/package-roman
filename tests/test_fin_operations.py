import json
from unittest.mock import MagicMock, patch

from fin_operations import reading_file_csv, reading_file_xlsx


class TestReadingFileCSV:
    """Тесты для функции чтения CSV файла"""

    @patch("pandas.read_csv")
    def test_reading_file_csv_success(self, mock_read_csv):
        # Создаем мок для Path
        mock_path = MagicMock()

        # Настраиваем поведение для path / "../transactions.csv"
        mock_div_result = MagicMock()
        mock_path.__truediv__.return_value = mock_div_result
        mock_div_result.resolve.return_value = "/fake/path/transactions.csv"

        # Настраиваем DataFrame
        test_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
        mock_df = MagicMock()
        mock_df.to_dict.return_value = test_data
        mock_read_csv.return_value = mock_df

        # Вызываем функцию с нашим моком Path
        result = reading_file_csv(mock_path)

        # Проверяем
        mock_path.__truediv__.assert_called_once_with("../transactions.csv")
        mock_div_result.resolve.assert_called_once()
        mock_read_csv.assert_called_once_with("/fake/path/transactions.csv", sep=";")
        assert result == json.dumps(test_data, ensure_ascii=False, indent=4)

    @patch("pandas.read_csv", side_effect=FileNotFoundError("File not found"))
    def test_reading_file_csv_file_not_found(self, mock_read_csv):
        # Создаем мок для Path
        mock_path = MagicMock()
        mock_path.__truediv__.return_value.resolve.return_value = "/fake/path"

        # Вызываем функцию
        result = reading_file_csv(mock_path)

        # Проверяем
        assert result is None


class TestReadingFileXLSX:
    """Тесты для функции чтения Excel файла"""

    @patch("pandas.read_excel")
    def test_reading_file_xlsx_success(self, mock_read_excel):
        # Создаем мок для Path
        mock_path = MagicMock()

        # Настраиваем поведение для path / "../transactions_excel.xlsx"
        mock_div_result = MagicMock()
        mock_path.__truediv__.return_value = mock_div_result
        mock_div_result.resolve.return_value = "/fake/path/transactions_excel.xlsx"

        # Настраиваем DataFrame
        test_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
        mock_df = MagicMock()
        mock_df.to_dict.return_value = test_data
        mock_read_excel.return_value = mock_df

        # Вызываем функцию с нашим моком Path
        result = reading_file_xlsx(mock_path)

        # Проверяем
        mock_path.__truediv__.assert_called_once_with("../transactions_excel.xlsx")
        mock_div_result.resolve.assert_called_once()
        mock_read_excel.assert_called_once_with("/fake/path/transactions_excel.xlsx")
        assert result == json.dumps(test_data, ensure_ascii=False, indent=4)

    @patch("pandas.read_excel", side_effect=FileNotFoundError("File not found"))
    def test_reading_file_xlsx_file_not_found(self, mock_read_excel):
        # Создаем мок для Path
        mock_path = MagicMock()
        mock_path.__truediv__.return_value.resolve.return_value = "/fake/path"

        # Вызываем функцию
        result = reading_file_xlsx(mock_path)

        # Проверяем
        assert result is None
