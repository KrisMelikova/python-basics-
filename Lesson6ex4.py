class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print("Машина повернула", direction)

    def  show_speed(self):
        print("Скорость авто:", self.speed)

class TownCar(Car):

    def  show_speed(self):
        if self.speed > 60:
            print("Вы превысили скорость!")
        else:
            print("Скорость авто:", self.speed)

class SportCar(Car):
    pass

class WorkCar(Car):

     def  show_speed(self):
        if self.speed > 60:
            print("Вы превысили скорость!")
        else:
            print("Скорость авто:", self.speed)

class PoliceCar(Car):
    pass

mazda = TownCar(65, "blue", "Mazda", False)
audi = SportCar(80, "yellow", "Audi", False)
kia = WorkCar(61, "red", "KIA", False)
ford = PoliceCar(50, "white", "Ford", True)


print(mazda.speed, mazda.color, mazda.name, mazda.is_police)
print(audi.speed, audi.color, audi.name, audi.is_police)
print(kia.speed, kia.color, kia.name, kia.is_police)
print(ford.speed, ford.color, ford.name, ford.is_police)

mazda.show_speed()
audi.show_speed()
kia.show_speed()
ford.show_speed()

mazda.go()
audi.stop()
kia.turn("направо")
ford.go()