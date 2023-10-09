import random as r
my_dict = {i:r.randint(0,100) for i in range(r.randint(5,10))}
ascending_dict = {}
descending_dict = {}
sorted_keys = sorted(my_dict, key=my_dict.get)
for i in sorted_keys:
	ascending_dict[i] = my_dict[i]
for i in sorted_keys[::-1]:
	descending_dict[i] = my_dict[i]
print('Исходный словарь:', my_dict)
print('В порядке возрастания:', ascending_dict)
print('В порядке убывания:', descending_dict)