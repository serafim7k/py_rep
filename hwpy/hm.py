list1 = []
list2 = ['winter', 'spring', 'summer']
list2.append('autumn')
print(list2[1])
list3 = [1, 2, 3, 4, 5]
all_list = list1, list2, list3
print(all_list)
del list2[1]
list2.insert(1, "summer")
print(list2)
input()