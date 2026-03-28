import requests
from requests import Response
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
from bs4.element import Tag
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


url = "https://spimex.com/markets/oil_products/trades/results/"


def get_xls_links(url: str, date_until: datetime):

    '''Парсит ссылки на бюллетени по итогам торгов за месяц, если они новее указанной даты'''

    html = connect_url(url)
    
    soup = BeautifulSoup(html.text, "html.parser")
    items = soup.select(".accordeon-inner__wrap-item")
 
    for item in items:
        link_tag = item.select_one("a.link.xls")
        if not link_tag:
            continue
        href = link_tag.get("href")

        date_tag = get_pdf_link_date(item) # выбираем тег с датой отчета
        if date_tag is None:
            continue

        if is_relevant(date_tag, date_until): #если дата отчета подходит возвращаем ссылку
            yield 'https://spimex.com' + href


def get_pdf_link_date(link_tag: Tag) -> datetime:
    """
    Вытаскивает дату из тега, преобразует в datetime
    """
    date_tag = link_tag.select_one(".accordeon-inner__item-inner__title p > span")
    if not date_tag:
            return None
    date_text = date_tag.text.strip().split(".")
    day, month, year = date_text
    file_date = datetime(year, month, day)

    return file_date


def get_xls_link_date(link_tag: Tag) -> datetime:

    """
    Вытаскивает дату из тега, преобразует в datetime
    """

    date_tag = link_tag.select_one(".accordeon-inner__item-inner__title p")
    if not date_tag:
        return None

    months = {
        "Январь": 1, "Февраль": 2, "Март": 3, "Апрель": 4,
        "Май": 5, "Июнь": 6, "Июль": 7, "Август": 8,
        "Сентябрь": 9, "Октябрь": 10, "Ноябрь": 11, "Декабрь": 12
    }

    date_text = date_tag.text.strip()
    parts = date_text.split()
    month = months.get(parts[0])
    year = int(parts[1])

    file_date = datetime(year=year, month=month, day=1)

    return file_date


def is_relevant(file_date: datetime, date_until: datetime) -> bool:

    if file_date >= date_until:
        return True
    return False



def connect_url(url: str) -> Response:
    try:
        html = requests.get(url)
        html.raise_for_status()
        
    except HTTPError as http_err:
        status_code = http_err.response.status_code
        if status_code == 404:
            logger.warning(f"Ресурс не найден: {url}")
            raise
        elif 400 <= status_code <= 500:
            logger.error(f"Клиентская ошибка: {http_err}")
            raise
        elif 500 <= status_code <= 600:
            logger.error(f"Серверная ошибка: {http_err}")
            raise

    return html
