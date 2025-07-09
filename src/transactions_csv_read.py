import csv


def reading_csv(file_path: str) -> list[dict]:
    """Функция, переводящая CSV-файл в список словарей"""
    new_list = []
    with open(file_path, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            new_list.append(row)
        return new_list
