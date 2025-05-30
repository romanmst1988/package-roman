def filter_by_state(list_inp: list[dict], state="EXECUTED") -> list[dict]:
    """
    Функция, которая фильтрует список словарей по значению ключа 'state'
    """
    new_list = []
    for i in list_inp:
        if i["state"] == state:
            new_list.append(i)
    return new_list


print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)


def sort_by_date(base_idtime: list[dict], reverse=False) -> list[dict]:
    """
    Функция, которая принимает список словарей и
    возвращает новый список, отсортированный по дате
    """
    return sorted(base_idtime, key=lambda x: x["date"], reverse=reverse)


print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
