import json
from pathlib import Path

import pandas as pd


def reading_file_csv(path_csv):
    """Функция, которая считывает финансовые операции из файла csv
    и выдает список словарей с транзакциями за тем возвращает их в виде json"""
    file_path = path_csv / "../transactions.csv"
    absolute_path = file_path.resolve()
    try:
        df = pd.read_csv(absolute_path, sep=";")
        js_dict = df.to_dict(orient="records")
        return json.dumps(js_dict, ensure_ascii=False, indent=4)

    except FileNotFoundError as file:
        print(f"Файл {file} не найден")
    return None


def reading_file_xlsx(path_xlsx):
    """Функция, которая считывает финансовые операции из файла xlsx
    и выдает список словарей с транзакциями за тем возвращает их в виде json"""
    file_path = path_xlsx / "../transactions_excel.xlsx"
    absolute_path = file_path.resolve()
    try:
        df = pd.read_excel(absolute_path)
        js_dict = df.to_dict(orient="records")
        return json.dumps(js_dict, ensure_ascii=False, indent=4)

    except FileNotFoundError as file:
        print(f"Файл {file} не найден")
    return None


if __name__ == "__main__":
    home_dir = Path.cwd()
    result_read_csv = reading_file_csv(home_dir)
    print(result_read_csv)


if __name__ == "__main__":
    home_dir_xlsx = Path.cwd()
    result_read_xlsx = reading_file_xlsx(home_dir_xlsx)
    print(result_read_xlsx)
