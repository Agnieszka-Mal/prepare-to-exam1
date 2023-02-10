class Calculator:

    def __init__(self):
        self.operations = []

    def add(self, num1:int, num2:int):
        result = num1 + num2
        operation = f" Wynik {num1} + {num2} = {result}"
        self.operations.append(operation)
        return result

    def multiply(self, num1:int, num2:int):
        result = num1 * num2
        operation = f" Wynik {num1} * {num2} = {result}"
        self.operations.append(operation)
        return result

    def print_operation(self):
        return self.operations


cal = Calculator()
cal.add(2, 2)
cal.multiply(2, 2)
print(cal.print_operation())
