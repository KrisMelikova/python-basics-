my_list = []
while True:
    a = int(input("Введите новый элемент рейтинга - натуральное число"))
    for i, el in enumerate(my_list):
        if el < a:
            my_list.insert(i, a)
            break
    else:
        my_list.append(a)
    print(my_list)