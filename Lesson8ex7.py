class ComplexNum:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real}+{self.imag}j"

    def __add__(self, other):
        return ComplexNum(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return ComplexNum((self.real * other.real - self.imag * other.imag), (self.imag * other.real + self.real * other.imag))

first = ComplexNum(2,3)
second = ComplexNum(4,-2)
print(first+second)
print(first*second)

