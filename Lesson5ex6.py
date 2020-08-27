import re

my_dict = {}

with open("text_6.txt", "r", encoding="utf-8") as content:
    for line in content.readlines():
        res_1 = line.split()
        res_2 = [el for el in res_1 if el != "-"]
        regex_num = re.compile('\d+')
        res_3 = regex_num.findall(line)
        time = 0
        for el in res_3:
            time = time + int(el)
        my_dict[res_1[0]] = time
print(my_dict)












