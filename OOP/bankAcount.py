class BankAccount:

    def __init__(self, number):
        self.number = number
        self.cash = 0.0

    def deposit_cash(self, amount):
        if amount > 0.0:
            self.cash += amount
            return round(self.cash, 2)
        else:
            return f"Kwota powinna być większa od ZERA"

    def withdraw_cash(self, amount):
        if amount > 0.0:
            if self.cash > amount:
                self.cash -= amount
                return round(self.cash, 2)
            elif self.cash < amount:
                self.cash -= self.cash
                return round(self.cash, 2)
        else:
            return f"Kwota powinna być większa od ZERA"

    def print_info(self):
        return f"numer konta: {self.number}, środki na koncie: {self.cash}."

x = BankAccount("78965")
print(x.deposit_cash(200))
print(x.withdraw_cash(-200))
print(x.print_info())