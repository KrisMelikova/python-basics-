class Storage(object):

    registration = {}

    def to_take(self, obj_class, amount):
        if obj_class not in self.registration:
            self.registration[obj_class] = obj_class()
        self.registration[obj_class].amount = self.registration[obj_class].amount + amount

    def to_give(self, obj_class, amount):
        if obj_class not in self.registration:
            raise Exception("На складе такого объекта нет")
        if self.registration[obj_class].amount < amount:
            raise Exception("На складе товара меньше запрошенного")
        self.registration[obj_class].amount = self.registration[obj_class].amount - amount

    def __str__(self):
       return "\n".join((f"{key.__class__}: {val}" for key, val in self.registration.items()))


class Equipment(object):

    amount = 0

    def __str__(self):
        return f"type:{self.__class__}, amount:{self.amount}"

class Printer(Equipment):

    to_print = "Печатаю"

class Scanner(Equipment):

    to_scan = "Сканирую"

class Xerox(Equipment):

    to_xerox = "Ксерокопирую"


equipment_mapping = {"Принтер": Printer, "Сканер": Scanner, "Ксерокс": Xerox}

storage = Storage()

while True:
    try:
        user_doing = input("Введите действие (положить/получить)")
        user_tech = input("Введите название техники")
        user_amount = input("Введите количество")
        if not user_amount.isdigit():
            raise Exception("Количество должно быть числом")
        user_amount = int(user_amount)
        tech_class = equipment_mapping[user_tech]
        if user_doing == "положить":
            storage.to_take(tech_class,user_amount)
        if user_doing == "получить":
            storage.to_give(tech_class, user_amount)
        print(storage)
    except Exception as e:
        print(e)



