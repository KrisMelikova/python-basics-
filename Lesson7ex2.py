from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def rate(self):
        pass

class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    def rate(self):
        self.rate_1 = self.size / 6.5 + 0.5
        return self.rate_1

class Costume(Clothes):

    def __init__(self, rize):
        self.rize = rize


    def rate(self):
        self.rate_2 = 2 * self.rize + 0.3
        return self.rate_2

    @property
    def my_method(self):
        return self.rize


first_coat = Coat(44)
print("%.2f" % first_coat.rate())


first_costume = Costume(180)
print("%.2f" % first_costume.rate())

print("Итого:","%.2f" % (first_coat.rate() +  first_costume.rate()))

print(first_costume.my_method)
