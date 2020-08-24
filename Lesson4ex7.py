def fact(n):
    prev = 1
    for el in range(1, n + 1):
        prev = prev * el
        yield el, prev

for el, fact in fact(4):
    print("%i! = %i" % (el, fact))