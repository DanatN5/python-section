from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from database import Base

class City(Base):
    __tablename__ = 'city'

    city_id: Mapped[int] = mapped_column(primary_key=True)

    name_city: Mapped[str]
    days_delivery: Mapped[int]

    clients: Mapped[List["Client"]] = relationship(back_populates="city", cascade="all, delete")



class Client(Base):
    __tablename__ = 'client'


    client_id: Mapped[int] = mapped_column(primary_key=True)

    name_client: Mapped[str]
    city_id: Mapped[int] = mapped_column(ForeignKey("city.city_id", ondelete="CASCADE"))
    email: Mapped[str]

    city: Mapped["City"] = relationship(back_populates="city")

