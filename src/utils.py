import json

from external_api import currency_convertor


def open_json(path: str) -> list:
    """Функция, которая преобразует JSON-объект в Python-объект"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []
    except Exception:
        return []




def convertor_to_rubles(operation: dict) -> float:
    """Функция, которая конвертирует валюту в рубли"""
    try:
        if operation["operationAmount"]["currency"]["code"] == "RUB":
            return float(operation["operationAmount"]["amount"])
        else:
            operation_currency = operation["operationAmount"]["currency"]["code"]
            operation_amount = operation["operationAmount"]["amount"]
            return float(currency_convertor(operation_currency, operation_amount))
    except (KeyError, ValueError):
        return 0.0



if __name__ == "__main__":
    print(open_json("../data/operations.json"))
    print(convertor_to_rubles({
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }}}))