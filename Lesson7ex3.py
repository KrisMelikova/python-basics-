class Cell:

    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        if self.cell < other.cell:
            return other.cell - self.cell
        else:
            return self.cell - other.cell

    def __mul__(self, other):
        return self.cell * other.cell

    def __floordiv__(self, other):
        if self.cell < other.cell:
            return other.cell // self.cell
        else:
            return self.cell // other.cell

    def make_order(self, rows):
      self.b = ""
      self.i = 0
      while self.i < self.cell:
          self.b = self.b + self.b.join("*")
          self.i += 1
      for x in range(0, len(self.b), rows):
          print(self.b[x:x+rows])

c_1 = Cell(25)
c_2 = Cell(40)
print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_1 // c_2)
c_1.make_order(4)
c_2.make_order(5)

