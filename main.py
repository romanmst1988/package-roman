# from src.masks import get_mask_account, get_mask_card_number
#
# print(get_mask_card_number("1234567812345678"))
#
# print(get_mask_account("123456"))
#


import json

# data - строка, тип str
data = '{"name": "John Smith", "age": 30, "city": "New York"}'
# parsed_data - словарь, тип dict
parsed_data = json.loads(data)

# Получаем значение словаря по ключу
print(parsed_data["name"], parsed_data["age"], parsed_data["city"])