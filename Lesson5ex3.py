text_doc = open("text_3.txt", "r", encoding="utf-8")
workers_count = 0
summary = 0

for line in text_doc.readlines():
    surname, salary = line.split(" ")
    if float(salary) <= 20000:
        print("Сотрудники с зарплатой менее 20000 руб.:", surname)
    workers_count +=1
    summary = summary + float(salary)

average = summary / workers_count
print("Средняя величина доходов сотрудников:", average, "руб.")
text_doc.close()







