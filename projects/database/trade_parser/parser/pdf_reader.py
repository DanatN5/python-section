import pandas as pd
import camelot
import numpy as  np

def pdf_reader(url: str) -> pd.DataFrame:
    tables = camelot.read_pdf(url, pages="all")
    dfs = [table.df for table in tables[2:]]
    df = pd.concat(dfs, ignore_index=True)

    return df


def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df[[0, 1, 2, 3, 4, 13]] # выбираем колонки

    # -- заменяем значения у колонки "Кол-во договоров"  на числа --
    df[13] = df[13].replace('-', np.nan).apply(pd.to_numeric, errors='coerce')

    filtered = df[df[13] > 0] # фильтруем по кол-ву договоров

    # -- приводим строки к типам" --
    filtered[3] = pd.to_numeric(filtered[3], errors='coerce')
    filtered[4] = pd.to_numeric(filtered[4], errors='coerce')
    filtered[13] = pd.to_numeric(filtered[13], errors='coerce')

    return filtered


