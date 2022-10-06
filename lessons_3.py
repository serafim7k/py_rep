# animal = 'dog'
# def print_global():
#     print('Global_name',animal)
#
# print(animal)
# print_global()
#
# def change_print_globa():
#     global animal
#     print('inside_func -', animal)
#     animal = 'cat'
#     print('After change:', animal)
#
# change_print_globa()
#
# def change_local():
#     animal = 'cat'
#     print('inside local:',animal)
#
# change_local()
# print(animal)

# def func(arg_1, arg_2, *args, **kwargs):
#     print(arg_1)
#     print(arg_2)
#     print(*args)
#     print(kwargs)
# func(25, 'dfgdf', True, name = 'misha', surename = 'Krotov', age = '25')

# def factorial(x):
#     """ This is func factorial. Recursiya"""
#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x - 1))
#
# print(factorial(6))
# print(factorial.__doc__)

def document_it(func):
    def new_func(*args, **kwargs):
        print('Args:', args)
        print('Kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_func


@document_it
def add_ints(a, b):
    c = a + b
    return c
print(add_ints(10, 20))
