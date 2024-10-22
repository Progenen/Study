lst = [('dasdas', 42), ('dasdas', 22),('dasdas', 44),('dasdas', 32),('dasdas', 11)]

res = sorted(lst, key=lambda x: x[1])
palidrom = list(map(lambda x: (((x[1] - x[1] % 10)) / 10) - (x[1] % 10) == 0 if x[1] else 0, lst))
maxNum = res[0]
minNum = res[-1]


print(palidrom)

print(res)

print(maxNum)
print(minNum)