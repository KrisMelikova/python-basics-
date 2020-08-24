orig_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list = [el for i, el in enumerate(orig_list) if i !=0 and orig_list[i] > orig_list[i-1]]
print(my_list)
