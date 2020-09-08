class MyOwnError(Exception):
    pass

my_list = []
user_data = 0
special = "q"

while True:
    user_data = input("Введите число, а если хотите выйти из программы нажмите q")
    if user_data == special:
        print("До свидания", my_list)
        break
    try:
        if user_data != special:
            if not user_data.isdigit():
               raise MyOwnError()
    except MyOwnError:
        print("Вводить нужно только числа")
    else:
        my_list.append(int(user_data))
        print(my_list)





