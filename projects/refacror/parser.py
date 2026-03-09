import datetime
from datetime import date

from bs4 import BeautifulSoup
from bs4.element import  Tag


def parse_page_links(html: str, start_date: date, end_date: date, url: str):
    """
    Парсит ссылки на бюллетени с одной страницы:
    <a class="accordeon-inner__item-title link xls" href="/upload/reports/oil_xls/oil_xls_20240101_test.xls">link1</a>
    """
    soup = BeautifulSoup(html, "html.parser")
    tags = soup.find_all("a", class_="accordeon-inner__item-title link xls")
    links = extract_and_purify_links(tags)

    results = [compare_link_date(link, start_date, end_date) for link in links]
        
    return results


def extract_and_purify_links(tags: list[Tag]) -> list[str]: 
    links = []
    for tag in tags:
        link = tag.get("href")
        if link:
            link = link.split("?")[0]
            if "/upload/reports/oil_xls/oil_xls_" not in link or not link.endswith(".xls"):
                continue
            links.append(link)



def compare_link_date(link: str, start_date: date, end_date: date) -> tuple:
    try:
        date = link.split("oil_xls_")[1][:8]
        file = datetime.datetime.strptime(date, "%Y%m%d").date()
        if start_date <= file <= end_date:
            u = link if link.startswith("http") else f"https://spimex.com{link}"
            return u, file
        else:
            print(f"Ссылка {link} вне диапазона дат")
    except Exception as e:
        print(f"Не удалось извлечь дату из ссылки {link}: {e}")
