info = []

while True:
    number = input("Введите номер товара")
    name = input("Введите название товара")
    price = input("Введите цену товара")
    quan = input("Введите количество товара")
    kind = input("Введите единицу товара")
    c = (number, {"название": name, "цена": price, "количество": quan, "единица": kind})
    info.append(c)
    print(info)
    k = {"название": [], "цена": [],"количество": [],"единица": [] }
    for number, item in info:
        k["название"].append(item["название"])
        k["цена"].append(item["цена"])
        k["количество"].append(item["количество"])
        k["единица"].append(item["единица"])
    print(k)