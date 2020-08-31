class Stationery:
    title = "Нечто"

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):

    def draw(self):
        print("Рисую ручкой")

class Pencil(Stationery):

    def draw(self):
        print("Рисую карандашом")

class Handle(Stationery):

    def draw(self):
        print("Рисую маркером")

var_1 = Pen()
var_2 = Pencil()
var_3 = Handle()

var_1.draw()
var_2.draw()
var_3.draw()


