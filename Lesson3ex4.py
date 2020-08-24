x = int(input("Введите действительное положительное число"))
y = int(input("Введите целое отрицательное число"))

if x <= 0 or y >= 0:
    print("Вы ввели неверные данные")
    exit(1)

def my_func(x,y):
    s = 1
    h = abs(y)-1
    a = x
    while s <= h:
        a = a * x
        s += 1
    return a

c = 1 / (my_func(x,y))

print(c)






"""
x = int(input("Введите действительное положительное число"))
y = int(input("Введите целое отрицательное число"))

с = x ** y

print(с)

"""


