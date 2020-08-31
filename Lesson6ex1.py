import time

class TrafficLight:
    __color = "red"
    __prev_color = ""

    def running(self):
        while True:
            print("Current color: %s" % self.__color)
            if self.__color == "red":
                time.sleep(7)
                self.__color = "yellow"
                self.__prev_color = "red"
            elif self.__color == "yellow":
                time.sleep(2)
                if self.__prev_color == "red":
                   self.__color = "green"
                else:
                    self.__color = "red"
            elif self.__color == "green":
                time.sleep(8)
                self.__color = "yellow"
                self.__prev_color = "green"

TL_1 = TrafficLight()
TL_1.running()

