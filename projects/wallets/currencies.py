from enum import Enum
from dataclasses import dataclass

class AvailableCurrencies(Enum):
    RUB = 'rub'
    USD = 'usd'


@dataclass(frozen=True, slots=True)
class Currency:
    code: AvailableCurrencies


@dataclass(frozen=True, slots=True)
class Rub(Currency):
    code: AvailableCurrencies = AvailableCurrencies.RUB



@dataclass(frozen=True, slots=True)
class Usd(Currency):
    code: AvailableCurrencies = AvailableCurrencies.USD


rub = Rub()
usd = Usd()



