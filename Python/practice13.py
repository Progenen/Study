import time

# Декоратор для измерения времени выполнения
def clock(func):
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)  # Вызов декорированной функции
        elapsed = time.time() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print(f'[{elapsed:.8f}s] {name}({arg_str}) -> {result!r}')
        return result
    return clocked

# Рекурсивный вариант
@clock
def sum_factorials_recursive(n):
    def factorial_recursive(x):
        if x == 0 or x == 1:
            return 1
        return x * factorial_recursive(x - 1)

    if n == 1:
        return 1
    return factorial_recursive(n) + sum_factorials_recursive(n - 1)

# Вариант с мемоизацией
@clock
def sum_factorials_memoized(n):
    cache = {}

    def factorial_memoized(x):
        if x in cache:
            return cache[x]
        if x == 0 or x == 1:
            cache[x] = 1
        else:
            cache[x] = x * factorial_memoized(x - 1)
        return cache[x]

    for i in range(1, n + 1):
        factorial_memoized(i)

    return sum(cache[i] for i in range(1, n + 1))

# Примеры вызовов
print(sum_factorials_memoized(100))
print(sum_factorials_recursive(100))

if (sum_factorials_memoized(200) > sum_factorials_recursive(200)):
    print("Рекурсия с меморизацией быстрее") 
else: 
    print("Рекурсися без меморизации быстрее")