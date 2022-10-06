list_1 = [5, 4.5, 'text', True, False]
print(list_1[0])
print(list_1[-1])
list_1.append(3)
list_1.remove(True)
list_1.remove(False)
print(list_1)

dict_1 = {
    'str': 'text_1',
    'str_1': 'text_2',
    'int': 5,
    'float': 4.5,
    'bool': True,
    'bool_1': False
}
print(dict_1['str'])
print(dict_1['bool_1'])
dict_1['int_1'] = 8
del dict_1['bool']
del dict_1['bool_1']
print(dict_1)
alfabet = "abcdefghijklmnopqrstuvwxyz"
print(alfabet.upper())
print(len(alfabet))
