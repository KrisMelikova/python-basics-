import json

with open("text_7.txt", "r", encoding="utf-8") as content:
    summary = 0
    total_count = 0
    my_dict = {}

    for line in content.readlines():
        name, form, income, loss = line.split()
        profit = int(income) - int(loss)
        my_dict[name] = profit
        if profit >= 0:
            summary = summary + profit
            total_count += 1
    average = summary / total_count

list_1 = [my_dict, {"average_profit": average}]

with open("text_77.json", "w", encoding="utf-8") as output:
    json.dump(list_1, output)

