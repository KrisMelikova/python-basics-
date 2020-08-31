with open("text_5.txt", "w", encoding="utf-8") as content:
    summary = 0
    numbers = "5 5 5 5 5 5 5 5"
    new_file = content.write(numbers)
    list_1 = numbers.split()
    for el in list_1:
        summary = summary + int(el)
    print(summary)


