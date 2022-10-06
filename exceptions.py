# a = int(input('input number_1: '))
# b = int(input('input number_2: '))

# if b == 0:
#     c = 'ZeroDivisionError'
# else:
#     c = a / b
# print('no error')
# print(c)

count = [1, 2, 3, 4]
count_1 = {1: 'one', 2: 'two'}

try:
    print(count[10])
except (IndexError):
    print('IndexError')
except (KeyError):
    print('KeyError')
else:
    print(count[2] + 10 - 2)
finally:
    print('All good!!!')
# print(c)
