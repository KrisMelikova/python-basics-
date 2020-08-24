user_words_1 = input("Введите слово, состоящее из маленьких латинский букв.")

def int_func (x):
    f = x.title()
    return f

print(int_func(user_words_1))

user_words_2 = input("Введите строку из слов, разделенных пробелом. Каждое слово должно состоять из латинских букв.")

print(int_func(user_words_2))