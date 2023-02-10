class Calculator:


    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

class LoggingCalculator(Calculator):

    def __init__(self):
        super().__init__()
        self.history = []

    def add(self, a, b):
        result = super().add(a, b)
        text1 = f"{a} + {b} = {result}"
        self.history.append(text1)
        return result

    def sub(self, a, b):
        result = super().sub(a, b)
        text1 = f"{a} - {b} = {result}"
        self.history.append(text1)
        return result

    def mul(self, a, b):
        result = super().mul(a, b)
        text1 = f"{a} * {b} = {result}"
        self.history.append(text1)
        return result

    def div(self, a, b):
        result = super().div(a, b)
        text1 = f"{a} / {b} = {result}"
        self.history.append(text1)
        return result


calc = LoggingCalculator()
print(calc.add(4, 5))
print(calc.mul(6, 4))
print(calc.sub(8, 4))
print(calc.div(4, 2))
print(calc.history)