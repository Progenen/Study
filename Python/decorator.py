def replace_if_equal(target_value, replacement_value):
    def decorator(func):
        def wrapper(arg):
            if arg == target_value:
                arg = replacement_value
            return func(arg)
        return wrapper
    return decorator

@replace_if_equal(-1, 0)
def my_function(x):
    print(f"x = {x}")

my_function(5)   # x = 5
my_function(-1)  # x = 0

def replace_if_equal(target_value):
    def decorator(func):
        def wrapper(arg):
            if arg == target_value:
                arg = func(arg)
        return wrapper
    return decorator

@replace_if_equal(-1, )
def my_function(x):
    print(f"x = {x}")

my_function(5)   # x = 5
my_function(-1)  # x = 0
