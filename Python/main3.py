
# x = float(input("Введите значение x: "))
# if -4 >= x <= 5:
#     print((x**2 + 6 * x)**(1/3) - 4)
# else:
#     print(x**5 + 3.5)


# a = int(input())
# b = int(input())
# res = a

# for i in range(a, b + 1):
#     res += i**2
    
# print(res)

# i = 0
# res2 = 0
# num = int(input())

# while num % 2 == 0:
#     res2 += num
#     num = int(input())


# print(res2)

# str = "Привет. Джон. Как. дела."
# strNew = ""
# count = 0

# for i in range(len(str)):
#     if (str[i] == "."):
#         str[i] == ""
#         count += 1
#     else:
#         strNew += str[i]

# print(count)
# print(strNew)

import functools
import random

a = []
i = 0

while i <= 4:
    a.append(random.randint(1, 20))
    i += 1

evenNums = list(filter(lambda x: x % 2 == 0 if x else 0, a))
summEvenNums = functools.reduce(lambda a, b: a + b, evenNums)

print(a)
print(evenNums)
print(summEvenNums)

lst1 = [3, 4, 5]
lst2 = [4, 5, 6]
lst3 = [3, 4, 5]

def lstSummFunc(a, b, c):
    return a + b + c

lstSumm = list(map(lstSummFunc, lst1, lst2, lst3))
lstSumm = list(map(lambda a, b, c: a + b +c, lst1, lst2, lst3))

print(lstSumm)