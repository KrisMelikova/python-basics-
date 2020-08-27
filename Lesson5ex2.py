text_doc = open("text_2.txt", "r", encoding="utf-8")
words = 0
lines = 0

for line in text_doc.readlines():
    lines = lines + 1
    words = words + len(line.split(" "))

print("Количество строк:", lines, "Количество слов:", words)

text_doc.close()

