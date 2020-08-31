class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._salary = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def get_full_name(self):
        info = " ".join((self.name, self.surname))
        return info

    def get_total_income(self):
        income = self._salary["wage"] + self._salary["bonus"]
        return income

first_worker = Position("Вася", "Петров", "директор", 10000, 500)
print("Работник:", first_worker.get_full_name())
print("Его зарплата в рублях:", first_worker.get_total_income())

