dict1 = {'t': 'ds', 'c':'ds','g':'dsaa'}
dict2 = {'t': 'ds', 'd': 32, 'g': 'dsaa'}

# 1
maxLen = max(len(value) for value in dict1.values())
keyLong = [key for key, value in dict1.items() if len(value) == max_len]
print("Ключи с самыми длинными значениями:",keyLong)

# 2
reversSort = dict(sorted(dict1.items(),reverse=True))
print("В обратном алфавитном порядке",reversSort)

# 3
symb = 't'
filter_d = {key:value for key, value in dict1.items() if key.startswith(symb)}
print(filter_d)

# 4
interSec = [item for item,]