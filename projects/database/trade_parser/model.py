from sqlalchemy import String, Computed, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class TradingResults(Base):
    __tablename__ = 'spimex_trading_results'

    id: Mapped[int] = mapped_column(primary_key=True)
    exchange_product_id: Mapped[str]
    exchange_product_name: Mapped[str]
    oil_id: Mapped[str] = mapped_column(
        Computed("LEFT(CAST(exchange_product_id AS TEXT), 4)"),
        nullable=False,
        type_=String(4)
    )
    delivery_basis_id: Mapped[str] = mapped_column(
        Computed("SUBSTRING(CAST(exchange_product_id AS TEXT) FROM 5 FOR 3)"),
        nullable=False,
        type_=String(3)
    )
    delivery_basis_name: Mapped[str]
    delivery_type_id: Mapped[int] = mapped_column(
        Computed("RIGHT(CAST(exchange_product_id AS TEXT), 1)"),
        nullable=False,
        type_=String(1)
    )

    volume: Mapped[int]
    total: Mapped[int]
    count: Mapped[int]

    date: Mapped[DateTime] = mapped_column(
        DateTime,
        default=func.now(),
        nullable=False,
    )
    created_on: Mapped[DateTime] = mapped_column(
        DateTime,
        default=func.now(),
        nullable=False,
    )
    updated_on: Mapped[DateTime] = mapped_column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
        nullable=False
    )
