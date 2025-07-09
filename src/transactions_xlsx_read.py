import pandas as pd


def reading_xlsx(file_path: str) -> list[dict]:
    """Функция, переводящая Excel-файл в список словарей"""
    df = pd.read_excel(file_path)
    result = df.to_dict(orient="records")
    return result
