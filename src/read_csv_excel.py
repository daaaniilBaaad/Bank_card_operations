import pandas as pd


def read_csv(file_path: str) -> list[dict]:
    """Функция, которая принимает данные с транзакциями из .csv файла"""
    df = pd.read_csv(file_path, delimiter=";")
    return df.to_dict(orient="records")


def read_excel(file_path: str) -> list[dict]:
    """Функция, которая принимает данные с транзакциями из .xlsx файла"""
    df = pd.read_excel(file_path)
    return df.to_dict(orient="records")
