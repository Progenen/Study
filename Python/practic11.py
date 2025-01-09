# class Fibonacci:
#     def __init__(self, n: int):
#         self.n = n

#     def __iter__(self):
#         return FibonacciIterator(self.n)
    

# class FibonacciIterator:
#     def __init__(self, n: int):
#         self.n = n
#         self.current, self.next = 0, 1

#     def __next__(self) -> int:
#         if self.n <= 0:
#             raise StopIteration()
        
#         self.n -= 1
#         current = self.current
#         self.current, self.next = self.next, self.next + self.current
#         return current
    
#     def __iter__(self):
#         return self
    

# fibo = Fibonacci(10)
# iterator = iter(fibo)
# print(isinstance(iterator, FibonacciIterator))

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for number in fibo:
#     print(number)

# print(sum(fibo))

# Генераторы
from collections.abc import Iterator

def fibnacci(n: int):
    current, next = 0, 1
    for _ in range(n):
        yield  current
        current, next = next, current + next

generator = fibnacci(10)
print(isinstance(generator, Iterator))

print(set(generator))