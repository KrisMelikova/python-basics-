# первый генератор

from itertools import count

for el in count(10):
    if el > 50:
        break
    else:
        print(el)

# второй генератор

from itertools import cycle

a = 0
for el in cycle("hi"):
    if a > 20:
        break
    print(el)
    a += 1


