i = 5
b = 4.5
t = "text"
list_1 = [i, b, t, False]
print(list_1[1])
tuple_1 = (5, 4.5, "text_2")
list_1 = tuple(list_1)
print(list_1)
dict_1 = {
          "int": 5,
          "float": 4.5,
          "str": "text_3",
          "bool": True,
          "list_2": [1, 2, 3, 4, 5],
          "bool_2": False
}
del dict_1["bool"]
del dict_1["bool_2"]
print(dict_1)
dict_1["int"] = 6
dict_1["float"] = 5.5
print(dict_1)