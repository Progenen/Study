import math

def f1(x):
    def inner_f1(y):
        return 1 + math.sin(x + y) ** 2
    return inner_f1

def f2(x):
    def inner_f2(y):
        denominator = 1 + x**2 * y**2
        return 2 + abs((x - 2 * x) / denominator)
    return inner_f2

def f(x):
    def inner_f(y):
        numerator = f1(x)(y)
        denominator = f2(x)(y)
        return numerator / denominator + x
    return inner_f

x_value = 1  
y_value = 2  

curried_f = f(x_value)  
result = curried_f(y_value) 

print(f"Результат f({x_value}, {y_value}) = {result}")