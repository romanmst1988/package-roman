import re
from collections import Counter


def search_transaction(operations: list[dict], search_string: str) -> list[dict]:
    """Функция, принимающая список словарей с данными об операциях и строку поиска,
    возвращающая список словарей, у которых в описании есть данная строка"""
    result = []
    re_pattern = re.compile(search_string, re.IGNORECASE)
    for operation in operations:
        if re_pattern.search(str(operation.get("description", ""))):
            result.append(operation)
    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция, принимающая список словарей с данными об операциях и список категорий операций,
    возвращающая словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории"""
    count_categories = []
    for operation in data:
        if operation.get("description", "") in categories:
            count_categories.append(operation.get("description", ""))
    return dict(Counter(count_categories))
