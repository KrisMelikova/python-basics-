from translate import Translator

with open("text_4.txt", "r", encoding="utf-8") as content:

    translator= Translator(to_lang = "Russian")

    new_file = open("new_text.txt", "w", encoding="utf-8")

    for line in content.readlines():
        a = line.split()
        a[0] = translator.translate(a[0])
        c = " ".join(a)
        print(new_file.write(c + "\n"))
    new_file.close()



