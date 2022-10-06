dict_1 = {
    'int': 5,
}
print(dict_1)
list_1 = ['Hello']
print(list_1)
tuple_1 = (4.5)
print(tuple_1)
set_1 = {1}
print(set_1)
a = 1
b = 100

if b > a:
    print('Умова виконується!!!')
elif b < a:
    print('Умова не виконується!!!')
elif b == a:
    print('Умова не виконується!!!')

if b == a:
    print("Йти метрів = ",  b)
else:
    print("Йти метрів = ",  a)

if b or a == True:
    print("Йти метрів = ",  b)
else:
    print("Йти метрів = ",  a)
