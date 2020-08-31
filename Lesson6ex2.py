class Road:

    _weight = 25
    _thickness = 5

    def __init__(self, a, b):
        self._length = a
        self._width = b

    def formula (self):
        return self._length * self._width * self._weight * self._thickness / 1000

result = Road(20, 5000)
print("Масса асфальта:", result.formula(), "тонн")
