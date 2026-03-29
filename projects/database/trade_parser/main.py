from config import DATE_UNTIL
from database import engine, Base, Session
from  model import TradingResults
from parser.parser import get_pdf_links
from  parser.pdf_reader import pdf_reader, prepare_data


URL = "https://spimex.com/markets/oil_products/trades/results/"


def init_db():
    Base.metadata.create_all(bind=engine)

def main() -> None:
    init_db
    for link in get_pdf_links(URL, DATE_UNTIL):
        file = pdf_reader(link)
        prepared_data = prepare_data(file)
        
        session = Session()
        records = prepare_data.to_dict(orient="records")
        session.bulk_insert_mappings(TradingResults, records)
        session.commit()




if __name__ == "__main__":
    main()