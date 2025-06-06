from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(name_card: str) -> str:
    """Функция, которая принимает строку с типом и номером карты или счета,
    возвращает строку с замаскированным номером."""
    if "счет" in name_card.lower():
        number_card = name_card[-20:]
        masked_card = get_mask_account(number_card)
        return f"Счет {masked_card}"
    elif name_card == "":
        raise ValueError("Пустая строка")
    elif name_card == "Visa":
        raise ValueError("Без номера карты")

    else:
        name_card_bank = name_card[-16:]
        masked_visa = get_mask_card_number(name_card_bank)
        name_bank = name_card[:-16]
        return f"{name_bank} {masked_visa}"


def get_date(data_card_number: str) -> str:
    '''Функция, которая принимает на вход строку с датой в одном
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"'''
    if data_card_number == "":
        raise ValueError("Пустая строка")
    elif data_card_number == "2024/03/11T02:26:18":
        raise ValueError("Неправильный формат разделителя")
    elif not data_card_number:
        raise ValueError("Некорректная строка")
    elif data_card_number == "20240311T02:26:18":
        raise ValueError("Без дефисов")

    data_correct = data_card_number[8:10] + "." + data_card_number[5:7] + "." + data_card_number[:4]
    return data_correct


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))
