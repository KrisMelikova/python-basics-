number = int(input("Введите целое положительное число"))

last_max_number = number % 10
number = number // 10

while number > 0:
    if number % 10 > last_max_number:
        last_max_number = number % 10
    number = number // 10

print(last_max_number)


# второй вариант решения задачи ниже:
# number = input("Введите целое положительное число")
# max_num2 = max(number, key = int)
# print(max_num2)


