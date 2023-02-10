class Employee:

    def __init__(self, id_, first_name, second_name):
        self.id = id_
        self.first_name = first_name
        self.second_name = second_name
        self._salary = 0

    @property
    def set_salary(self):
        return self._salary

    @set_salary.setter
    def set_salary(self, salary):
        if isinstance(salary, int) and salary > 0.0 and isinstance(salary, int) and salary > 0.0:
            self._salary = salary
        else:
            print("Invalid data")

    #@staticmethod
    #def check_salary(salary):
        #return salary >= 0.0 and type(salary) == float


m = Employee(1, "Aga", "kowalska")
m.set_salary = 10
m.set_salary = 20
print(m._salary)



