print("Задание #1")


def upLowSym(string_):
    upperSym = map(str.upper, string_)
    lowerSym = map(str.lower, string_)

    trash = set() 
    result = []

    for char in list(upperSym) + list(lowerSym):
        if char not in trash:
            trash.add(char)
            result.append(char)
    return result


string_ = ["a", "b", "E", "f", "a", "i", "o", "U", "a"]
result = upLowSym(string_)
print(result, "\n")

print("Задание #2 Фибоначи")


def fibonacci(n):
    fib_ = []
    a, b = 0, 1
    for i in range(n):
        fib_.append(a)
        a, b = b, a + b
    return fib_


def square(num):
    return num**2


N = 10
fibNums = fibonacci(N)
squareFib = list(map(square, fibNums))
print(squareFib, "\n")

print("Задание #3 Квадрат")
nums3 = [1, 2, 3, 4, 5, 6]

square_nums3 = list(map(square, nums3))
print(square_nums3, "\n")


print("Задание #4 reduce, filter")

from functools import reduce


def is_two(n):
    return 10 <= abs(n) < 100


def proizvedenie(a, b):
    return a * b


nums4 = [1, 20, 10, -5, -10]

digits = sorted(filter(is_two, nums4))
print("Двухзначные числа: ", nums4)

if digits:
    _ = reduce(proizvedenie, digits)
else:
    _ = 0

print("Произведение двухзначных чисел: ", _, "\n")


print("DZ #5 ")

nums5 = [1, 25, 10, -7, 88, -34, 8, 13]


def is_index(index):
    return index % 2 == 0


indexChet = [k for index, k in enumerate(nums5) if is_index(index)]

sortedNums5 = sorted(indexChet)

print("Четные позиции: ", sortedNums5)

def sum_of_two(a, b):
    return a + b


if sortedNums5:
    total = reduce(sum_of_two, sortedNums5)
else:
    total = 0

print('Сумма чисел четных позиций: ', total)