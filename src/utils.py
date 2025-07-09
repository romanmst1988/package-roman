import json

from external_api import currency_convertor

# import logging


# logger = logging.getLogger("utils")
# file_handler = logging.FileHandler("../logs/utils.log", encoding="utf-8")
# file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
# file_handler.setFormatter(file_formatter)
# logger.addHandler(file_handler)
# logger.setLevel(logging.DEBUG)


def open_json(path: str) -> list:
    """Функция, которая преобразует JSON-объект в Python-объект"""
    try:
        # logger.debug("Вывод списка словарей с данными о финансовых транзакциях из файла operations.json")
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # logger.debug("Список не найден в файле operations.json")
        return []
    except Exception:
        # logger.error("Ошибка при чтении файла operations.json")
        return []


def convertor_to_rubles(operation: dict) -> float:
    """Функция, которая конвертирует валюту в рубли"""
    try:
        # logger.debug("Конвертация суммы транзакции в рубли")
        if operation["operationAmount"]["currency"]["code"] == "RUB":
            return float(operation["operationAmount"]["amount"])
        else:
            operation_currency = operation["operationAmount"]["currency"]["code"]
            operation_amount = operation["operationAmount"]["amount"]
            # logger.debug(f"Конвертация суммы транзакции из {operation_currency} в рубли")
            return float(currency_convertor(operation_currency, operation_amount))
    except (KeyError, ValueError):
        # logger.error("Ошибка при конвертации суммы транзакции в рубли")
        return 0.0


if __name__ == "__main__":
    print(open_json("../data/operations.json"))
    print(
        convertor_to_rubles(
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            }
        )
    )
