import book
import buy_book
import client
from database import engine, Base

def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()