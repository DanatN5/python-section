import requests
from requests import Response
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
from bs4.element import Tag
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


def get_pdf_links(url: str, date_until: datetime):

    '''Парсит ссылки на бюллетени по итогам торгов за месяц, если они новее указанной даты'''
    while True:

        html = connect_url(url)
        
        soup = BeautifulSoup(html.text, "html.parser")
        items = soup.select(".accordeon-inner__wrap-item")
    
        for item in items:
            link_tag = item.select_one("a.link.pdf")
            if not link_tag:
                continue
            href = link_tag.get("href")

            date_tag = get_pdf_link_date(item) # выбираем тег с датой отчета
            if date_tag is None:
                continue

            if not is_relevant(date_tag, date_until): #если дата отчета подходит возвращаем ссылку
                return
            yield 'https://spimex.com' + href

        next_page = soup.select_one(".bx-pag-next a").get("href")
        url = 'https://spimex.com' + next_page


def get_pdf_link_date(link_tag: Tag) -> datetime:
    """
    Вытаскивает дату из тега, преобразует в datetime
    """
    date_tag = link_tag.select_one(".accordeon-inner__item-inner__title p > span")
    if not date_tag:
            return None
    date_text = date_tag.text.strip().split(".")
    day, month, year = date_text
    file_date = datetime(int(year), int(month), int(day))

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
