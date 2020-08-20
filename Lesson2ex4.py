a = input("Введите строку из нескольких слов, разделённых пробелами")
b = a.split()

for ind, el in enumerate(b):
    print(ind, el[0:10])

