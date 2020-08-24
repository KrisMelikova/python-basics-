a = int(input("Введите первое число"))
b = int(input("Введите второе число"))

def my_func(a,b):
        h = a / b
        return h

try:
    print("Результат деления первого числа на второе: ", round(my_func(a,b), 2))
except ZeroDivisionError:
    print("Делить на ноль нельзя! Попробуйте заново.")