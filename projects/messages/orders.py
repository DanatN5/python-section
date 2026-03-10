from dataclasses import dataclass

@dataclass
class LoyaltyDiscount:
    value: float = 0.1


@dataclass
class PercentDiscount:
    value: float = 0.1

@dataclass
class FixedDiscount:
    value: float = 0.1

@dataclass
class Order:
    """There is no need to describe anything here."""
    priece: float
    loyalty_dc: LoyaltyDiscount | int = 0
    percent_dc: PercentDiscount | int = 0
    fixed_dc: FixedDiscount | int = 0

    def total(self):
        if not isinstance(self.loyalty_dc, int):
            loyalty_dc = self.priece * self.loyalty_dc.value

        if not isinstance(self.percent_dc, int):
            percent_dc = self.priece * self.percent_dc.value

        if not isinstance(self.fixed_dc, int):
            fixed_dc = self.priece * self.fixed_dc.value

        return self.priece - (fixed_dc + percent_dc + loyalty_dc)
    
