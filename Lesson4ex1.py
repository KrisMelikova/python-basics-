from sys import argv

script_name, time, wage_rate, premium = argv

time = int(time)
wage_rate = int(wage_rate)
premium = int(premium)

salary = time * wage_rate + premium

print("Зарплата сотрудника за указанные часы:", salary, "руб.")

