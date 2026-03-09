from dataclasses import dataclass
from wallets.exceptions import NotComparisonException, NegativeValueException
from wallets.currencies import rub, usd, Currency

@dataclass(frozen=True)
class Money:
    value: int
    currency: Currency
        
    def check_currency(self, other):
        if self.currency != other.currency:
            raise NotComparisonException

    def __add__(self, other):
        self.check_currency(other)
        new_value = self.value + other.value
        return Money(new_value, self.currency)
    
    def __sub__(self, other):
        self.check_currency(other)
        new_value = self.value - other.value
        return Money(new_value, self.currency)
    
    def is_negative(self):
        return self.value < 0


class Wallet:
    def __init__(self, money: Money = None):
        self.currencies = {
            rub: Money(value=0, currency=rub),
            usd: Money(value=0, currency=usd),
        }
        if money:
            self.currencies[money.currency] += money


    def __getitem__(self, item):
        if isinstance(item, Currency):
            return self.currencies[item]
        
    def __delitem__(self, item):
        if isinstance(item, Currency):
            del self.currencies[item]

    def __contains__(self, item):
        return item in self.currencies.keys()
    
    def __len__(self):
        return len(self.currencies)

            

    def add(self, money: Money):
        self.currencies[money.currency] += money
        return self

    def sub(self, money):
        val = self.currencies[money.currency] - money
        if self.currencies[money.currency].is_negative():
            raise NegativeValueException
        self.currencies[money.currency] = val
        return self


