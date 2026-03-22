from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import List

from client import Client
from book import Book
from database import Base

class Buy(Base):
    __tablename__ = 'buy'

    buy_id: Mapped[int] = mapped_column(primary_key=True)
    
    buy_description: Mapped[str]
    client_id: Mapped[int] = mapped_column(ForeignKey("client.client_id", ondelete="SET NULL"))

    client: Mapped["Client"] = relationship()


class Step(Base):
    __tablename__ = 'step'

    step_id: Mapped[int] = mapped_column(primary_key=True)
    
    name_step: Mapped[str]


class BuyStep(Base):
    __tablename__ = 'buy_step'

    buy_step_id: Mapped[int] = mapped_column(primary_key=True)

    buy_id: Mapped[int] = mapped_column(ForeignKey("buy.buy_id"))
    step_id: Mapped[int] = mapped_column(ForeignKey("step.step_id"))
    date_step_bed: Mapped[datetime]
    date_step_end: Mapped[datetime]

    buy: Mapped["Buy"] = relationship()
    step: Mapped["Step"] = relationship()


class BuyBook(Base):
    __tablename__ = 'buy_book'

    buy_book_id: Mapped[int] = mapped_column(primary_key=True)

    buy_id: Mapped[int] = mapped_column(ForeignKey("buy.buy_id"))
    book_id: Mapped[int] = mapped_column(ForeignKey("book.book_id"))
    amount: Mapped[int]

    buy: Mapped["Buy"] = relationship()
    books: Mapped[List["Book"]] = relationship()
