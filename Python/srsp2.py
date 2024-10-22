listD = [2, 3, 4, 6, 9, 5]
input1 = int(input())

listRes1 = list(filter(lambda x: x % 2 != 0 if x else 0, listD))
listRes1Summ = sum(listRes1)
listRes2 = list(filter(lambda x: x % input1 == 0 if x else 0, listRes1))
    
print(listRes1)
print(listRes1Summ)
print(listRes2)

# listD = []
# i = 0

# while i <= 5:
#     listD.append(input())
#     i += 1

# listNew = list(filter(lambda x: isinstance(x, int) == True if x else len(x), listD))

# print(listNew)
