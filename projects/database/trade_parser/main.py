from config import DATE_UNTIL
from database import engine, Base, Session
from  model import TradingResults
from parser.parser import get_pdf_links
from  parser.pdf_reader import pdf_reader, prepare_data


URL = "https://spimex.com/markets/oil_products/trades/results/"




def main() -> None:
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


    for link in get_pdf_links(URL, DATE_UNTIL):
        file = pdf_reader(link)
        prepared_data = prepare_data(file)
        
        session = Session()
        for _, row in prepared_data.iterrows():
            record = TradingResults(
                exchange_product_id=row[0],
                exchange_product_name=row[1],
                delivery_basis_name=row[2],
                volume=row[3],
                total=row[4],
                count=row[13]
            )
            session.add(record)
        
        session.commit()




if __name__ == "__main__":
    main()