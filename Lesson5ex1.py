my_file = open("Lesson1.txt", "w")

while True:
    user_info = input("Введите данные")
    if len(user_info) == 0:
        break
    else:
        content = my_file.write(user_info + "\n")
        print(content)

my_file.close()
