import os

import requests
from dotenv import load_dotenv

load_dotenv()


def currency_convertor(currency: str, amount: float) -> float:
    """Функция, которая обращается к API для получения текущего курса валюты и конвертации"""
    new_currency = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={new_currency}&from={currency}&amount={amount}"

    payload = {}
    headers = {"apikey": os.getenv("API_KEY_LAYER")}

    response = requests.request("GET", url, headers=headers, data=payload)

    return float(response.json()["result"])


if __name__ == "__main__":
    print(currency_convertor("USD", 100))
    print(type(currency_convertor("USD", 100)))
