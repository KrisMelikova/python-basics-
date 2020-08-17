a = []

while len(a) < 9:
    a.append(input("Введите 9 элементов списка"))

print("Вы ввели:", a)

for i in range(len(a)):
    if (i + 1) % 2 == 0:
        a[i], a[i-1] = a[i-1], a[i]

print("Итоговый список:", a)


