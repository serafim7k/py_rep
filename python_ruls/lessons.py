from calendar import weekday


name = "Mark"
s_name = "Jun"
age = 16
id(age)
id(name)
hello = "Hi, {} {}!".format(name,s_name)
hello_2 = f"{name} has {age} year!"
print(hello)
print(hello_2)
list()
empty_list = []
not_empty_list = [1,"Hello",True,2.6,"Jone"]
print(not_empty_list)
print(list("cat"))
weekday = ["Monday","Tuesdy","Wednesday","Friday"]
print(weekday)
print(weekday[0])
print(weekday[-1])
print(weekday[0:3])
print(weekday.append('saturday'))
print(weekday)
weekday.insert(0,"sanday")
print(weekday)
del weekday[0]
print(weekday)
weekday.remove("Friday")
print(weekday)
print("dsfdsfs" in weekday)

list_1 = ['fridar', 23, 1.3, True]
print(list_1)
list_1.append(False)
print(list_1)
# кортежи
tuple_1 = (2, 'dog', 2.5, 'cat')
print(tuple_1)
# словники
dict_1 = {'day_1':'monday',
          'week': ['one', 'two', 'three', 'four'],
          3: 'mounth'
          }
print(dict_1)
print(dict_1["day_1"])
print(dict_1[3])
dict_1[4] = 'seasson'
print(dict_1)
dict_1[3] = 'mounth_new'
print(dict_1)
del dict_1['day_1']
print(dict_1)
# dict_1.clear()
# print(dict_1)
print(dict_1.get(3))
print(dict_1.keys())
print(dict_1.values())
print(dict_1.items())
print(4 in dict_1)
users = {
        'name': 'Mark',
        'phone': 25156554,
        'id': 213
        }
# множини
set_1 = {1,2,25,42,2,1,1,1,2}
print(set_1)
set_1.add(100)
print(set_1)
set_2 = {22,42,1000}
print(set_2)
# ті які повторяються
print(set_1 & set_2)
# об'єдненя
print(set_1 | set_2)
# не змінюваний
frozenset_1 = frozenset([1,58,25,100])
print(frozenset_1)
# оператори
# + - * / // ** %
#
print(False | False)
# += -= *= /= **= //= %=
a = 0
while a < 10:
    a += 1
    print(a)
#and or not in
tuple_2 = 2, 2
print(list())