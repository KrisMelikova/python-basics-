def my_func(a,b,c):
    list_my_func = [a,b,c]
    min_1 = min(list_my_func)
    list_my_func.remove(min_1)
    summ = sum(list_my_func)
    return summ

print(my_func(10, 80, 50))
