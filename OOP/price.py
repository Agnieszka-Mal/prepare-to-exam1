class Price:

    def __init__(self, price):
        self.price_PLN = price

    @property
    def price_PLN(self):
        return f"{self._price: .2f} PLN"

    @price_PLN.setter
    def price_PLN(self, value):
        self.value = float(value)
        self._price = value

    @property
    def price_EUR(self):
        return f"{self._price / 4.5: .2f} EUR"

    @price_EUR.setter
    def price_EUR(self, value):
        self.price_PLN = value * 4.5

    @property
    def price_USD(self):
        return f"{self._price / 3.8: .2f} USD"

    @price_USD.setter
    def price_USD(self, value):
        self.price_PLN = value * 3.8

    def __str__(self):
        return f"{self._price} PLN"


p = Price(2)
p.price_PLN = 100
print(p.price_EUR)
print(p.price_USD)
p.price_EUR = 100
print(p.price_PLN)
p.price_USD = 100
print(p.price_PLN)
print(p.__str__())