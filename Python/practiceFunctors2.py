# class Formatter:
#     def __init__(self, template):
#         self.template = template

#     def __call__(self, **kwargs):
#         result = self.template
#         for key, value in kwargs.items():
#             placeholder = "{" + key + "}"
#             result = result.replace(placeholder, str(value))
#         return result
    

# formatter = Formatter("Привет, {name}! Твой баланс: {balance} рублей.")

# result = formatter(name="Алексей", balance=100)
# print(result)

class SaveLast:
    def __init__(self, func, *args):
        self.func = func
        self.last_res = None
        self.has_res = False

        if not args and self.has_res:
            return self.last_res
        
        self.last_res = self.func(*args)
        self.has_res = True

    def __call__(self):
        if self.has_res:
            return self.last_res
        else: 
            return False


def sum (a, b):
    return a + b

word = SaveLast(sum, 2)

print(word())
    
    
