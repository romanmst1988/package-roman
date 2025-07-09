from generators import filter_by_currency
from processing import filter_by_state, sort_by_date
from bank_read_file import search_transaction
from fin_operations import reading_file_csv, reading_file_xlsx
from transactions_csv_read import reading_csv
from transactions_xlsx_read import reading_xlsx
from utils import open_json
from widget import mask_account_card, get_date


def main():
    """Функция, обрабатывающая файл и отфильтровывающая список операций
    по нескольким критериям и скрывающая номера реквизитов"""
    print(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями!
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла\n"""
    )

    user_input_first = input("Выберите необходимый пункт меню: ")

    if user_input_first == "1":
        print("Выбран JSON-файл для обработки\n")
        operation_list = open_json("C:/Users/Admin/PycharmProjects/package-roman/data/operations.json")
    elif user_input_first == "2":
        print("Выбран CSV-файл для обработки\n")
        operation_list = reading_csv("C:/Users/Admin/PycharmProjects/package-roman/transactions.csv")
    else:
        print("Выбран XLSX-файл для обработки\n")
        operation_list = reading_xlsx("C:/Users/Admin/PycharmProjects/package-roman/transactions_excel.xlsx")
    print(
        """
Необходимо выполнить фильтрацию по статусу.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
    """
    )
    user_input_status = input("Введите статус: ")
    while user_input_status.upper() not in ("EXECUTED", "CANCELED", "PENDING"):
        print("""Статус ошибочный! Введите доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n""")
        user_input_status = input("Введите статус: ")
    filtered_by_state_list = filter_by_state(operation_list, user_input_status.upper())
    print(f"Операции отфильтрованы по статусу - {user_input_status.upper()}\n")

    print("Отсортировать операции по дате? Да / Нет: ")
    input_sort_by_date = input("Сортируем? ").lower()
    while input_sort_by_date not in ("да", "нет"):
        print("Выберите один из предложенных вариантов\n")
        input_sort_by_date = input("Сортируем? ").lower()
        if input_sort_by_date == "да":
            input_sort_by_date_ = input(
                "Отсортировать по возрастанию или по убыванию?\n"
                "Ответьте 'Да', если по возрастанию, или 'Нет', если по убыванию: "
            ).lower()
            while input_sort_by_date_ not in ("да", "нет"):
                print("Выберите один из предложенных вариантов\n")
                input_sort_by_date_ = input(
                    """
Отсортировать по возрастанию или по убыванию?
Ответьте 'Да', если по возрастанию, или 'Нет', если по убыванию:
                """
                ).lower()
                if input_sort_by_date_ == "да":
                    filtered_by_state_list = sort_by_date(filtered_by_state_list, False)
                else:
                    filtered_by_state_list = sort_by_date(filtered_by_state_list)

    print("Выводить только рублевые транзакции? Да/Нет: ")

    input_filter_by_currency = input("").lower()
    if input_filter_by_currency == "да":
        filtered_by_state_list = list(filter_by_currency(filtered_by_state_list, "RUB"))

    print("Отфильтровать список транзакций по определенному слову в описании? Да / Нет: ")
    input_word_filter = input("").lower()
    if input_word_filter == "да":
        input_word_search = input("Введите слово или ряд букв для поиска: ")
        filtered_by_state_list = search_transaction(filtered_by_state_list, input_word_search)
    else:
        print("Фильтрация не будет применена!\n")

    print("Распечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(filtered_by_state_list)}\n")

    for i in filtered_by_state_list:
        from_ = mask_account_card(str(i.get("from", ""))) + " -> " if i.get("from") else ""
        date_ = i.get("date") or "По умолчанию"
        description_ = i.get("description") or "По умолчанию"
        amount_ = i.get("operationAmount", {}).get("amount") or i.get("amount")
        to_ = i.get("to") or "По умолчанию"
        currency_code_ = i.get("currency_code") or i.get("operationAmount", {}).get("currency", {}).get("name")

        print(
            f"{get_date(date_)} {description_}\n"
            f"{from_}{mask_account_card(str(to_))}\n"
            f"Сумма: {amount_} {currency_code_}\n"
        )

if __name__ == "__main__":
    print(main())