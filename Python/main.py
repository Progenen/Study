from modules.numWork import is_lucky_number, can_form_word, print_military_employees
import modules.numWork as lib
from importlib import reload 
from modules.module import squareTriangle 

reload(lib)

# employees = [
#     ("Иванов", "военнообязанный"),
#     ("Петров", "невоеннообязанный"),
#     ("Сидоров", "военнообязанный")
# ]

# print_military_employees(employees)
# print(is_lucky_number(100001))
# print(can_form_word("лес", "сел"))

print(squareTriangle(4, 4, 5))