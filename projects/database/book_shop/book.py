from sqlalchemy import ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import List
from database import Base


class Author(Base):
    __tablename__ = 'author'

    author_id: Mapped[int] = mapped_column(primary_key=True)
    name_author: Mapped[str] = mapped_column(String(30))
    books: Mapped[List["Book"]] = relationship(back_populates="author", cascade="all, delete")


    def __repr__(self):
        return f"{self.name_author}"

class Genre(Base):
    __tablename__ = 'genre'

    genre_id: Mapped[int] = mapped_column(primary_key=True)
    name_genre: Mapped[str]


class Book(Base):
    __tablename__ = 'book'

    book_id: Mapped[int] = mapped_column(primary_key=True)
    
    title: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("author.author_id", ondelete="CASCADE"))
    genre_id: Mapped[int] = mapped_column(ForeignKey("genre.genre_id"))
    price: Mapped[float]
    amount: Mapped[int]

    genres: Mapped[List["Genre"]] = relationship()
    author: Mapped["Author"] = relationship(back_populates="books")
    
