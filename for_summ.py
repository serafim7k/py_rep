# n = int(input("Enter number: "))
#
# s = 0
#
# for i in range(1, n + 1):
#     s = s + i / (2 * i + 1)
#
# print("Summ", s)

s = 0

for i in range(1, 11):
    for j in range(1, 6):
        s = s + i / (i + j ** 2)

print("Summ", s)

dict_ = {i: i ** 2 for i in range(10) if i == 8}

print(dict_)
