class MyOwnError(Exception):
    pass

user_data_1 = int(input("Введите делимое"))
user_data_2 = int(input("Введите делитель"))

try:
    if user_data_2 == 0:
        raise MyOwnError("Вы ввели 0, а делить на 0 нельзя!")
    result = user_data_1 / user_data_2
    print(round(result))
except MyOwnError:
    print("Вы ввели 0, а делить на 0 нельзя!")


