distance_per_day = int(input("Введите количество километров, которое Вы пробежали в первый день"))
total = int(input("Введите итоговое желаемое количество километров, которое Вы хотите пробежать"))
day = 0
runned = 0

while runned < total:
    runned = runned + distance_per_day
    distance_per_day = distance_per_day * 1.1
    day += 1
    print("%s day, %s km" % (day, runned))
print("Вы пробежите", total, "км", "за следующее количество дней:", day)