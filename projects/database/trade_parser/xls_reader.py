import pandas as pd


from parser import get_xls_links
from datetime import datetime

url = "https://spimex.com/markets/oil_products/trades/results/"

sheet = pd.read_excel("/home/danat5/bys4e9qvx8ug6geet0yb2gxgn1hcw3k6.xls",
                      sheet_name="Объёмы договоров в ед измерения")

links = get_xls_links(url, datetime(2025, 12, 1))

sheet2 = pd.read_excel(next(links))

print(sheet.info())