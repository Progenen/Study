import random
from functools import reduce

N = int(input) 


random_list = [random.randint(1, 50) for _ in range(N)]
print(f"Исходный список: {random_list}")

sorted_list = sorted(random_list)
print(sorted_list)

multiples_of_five = list(filter(lambda x: x % 5 == 0, sorted_list))
count_multiples_of_five = len(multiples_of_five)
print(multiples_of_five)
print(count_multiples_of_five)