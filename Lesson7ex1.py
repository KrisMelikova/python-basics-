class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return ( " ".join(map(str,self.matrix[0])) + "\n"
                 + " ".join(map(str,self.matrix[1])) + "\n"
                 + " ".join(map(str, self.matrix[2])) + "\n")

    def __add__(self, other):
        return ( [[self.matrix[0][0] + other.matrix[0][0],
                 self.matrix[0][1] + other.matrix[0][1]],
                 [self.matrix[1][0] + other.matrix[1][0],
                 self.matrix[1][1] + other.matrix[1][1]],
                 [self.matrix[2][0] + other.matrix[2][0],
                 self.matrix[2][1] + other.matrix[2][1]]])

mat_1 = Matrix([[1, 5], [3, 4], [1, 2]])
mat_2 = Matrix([[3, 2], [1, 3], [4, 5]])
print(mat_1.__str__())
print(mat_2.__str__())
mat_3 = Matrix(mat_1+mat_2)
print("Результат сложения двух матриц:" + "\n" + mat_3.__str__())
