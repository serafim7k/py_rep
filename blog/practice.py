import random

# list_ = []
# dict_ = {12: 21, }
# set_ = {12,21}
# list_.append("hello")
# print(list_)
# dict_[21] = 12
# print(dict_)
# set_.add(324)
# print(set_)
# tuple_ = (1, True, "Hi")

# a = 10
# b = 20
# c = 15

# if b > a and c > a and b == c:
#     print("True")
# else:
#     print("False")

# a = 0
#
# while a <= 5:
#     print("Hi")
#     a += 1
# print(a)

# list_ = [1, 'hello', 1.5, True]

# for i in range(0, len(list_)):
#     print(list_[i])
#
# for i in list_:
#     print(i)
#
# for i in range(20, 0, -1):
#     print(i)

# a = int(input("Enter Number: "))

# def sumFor(a, b = 0):
#     for i in range(a + 1):
#         b += i
#     return b
#
# print(sumFor(a))

# 0 <= 1
a = random.random()

# x <= y   +/- a
b = random.randrange(100, 1000, 50)

# x <= y
c = random.randint(0, 300)

e = random.choice("Hello World")

i = random.choice([1, 'hello', 1.5, True, 6, False])

g = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

random.shuffle(g)

print(a)
print(b)
print(c)
print(e)
print(i)
print(g)

def funk(x1, x2=8):
    print(x1)
    print(x2)

print(funk(1, 4))