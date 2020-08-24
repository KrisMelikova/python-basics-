summ = 0
special = "q"
w = False

while True:
    a = input("Введите строку чисел через пробел")
    b = a.split()

    for el in b:
        if el == special:
            w = True
            continue
        summ = summ + int(el)

    print(summ)

    if w is True:
        break





