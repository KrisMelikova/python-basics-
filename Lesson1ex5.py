proceeds = int(input("Введите значение выручки Вашей фирмы в рублях"))
costs = int(input("Введите значение издержек Вашей фирмы в рублях"))

if proceeds > costs:
    print("Отлично, Ваша фирма прибыльна!")
    profit = proceeds - costs
    effic = profit / proceeds * 100
    print ("Рентабельность выручки Вашей фирмы равна:", effic, "%")
    employee = int(input("Введите количество сотрудников фирмы"))
    prof_emp = profit / employee
    print("Прибыль фирмы в расчете на одного сотрудника равна:", round(prof_emp), "руб.")
else:
    print("Ваша фирма работает в убыток.")
