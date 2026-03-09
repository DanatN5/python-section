class NotComparisonException(Exception):
    def __init__(self):
        self.message = 'Операции с различающимися валютами не поддерживаются'

    def __str__(self):
        return self.message
    

class NegativeValueException(Exception):
    def __init__(self):
        self.message = 'Неостаточно средств'

    def __str__(self):
        return self.message
    