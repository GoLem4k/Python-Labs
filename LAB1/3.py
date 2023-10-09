import math as m

my_list = [1,34, 'qwerty', 12, 13, 16, 'Love', 'Python']
int_list = []
str_list = []

for i in my_list:
	if type(i) is int:
		int_list.append(i)
	elif type(i) is str:
		str_list.append(i)
print('Список из int:', int_list)
print('Список из str:', str_list)

print('Сумма:', sum(int_list))
print('Произведение:', m.prod(int_list))

print('Три наибольших элемента:')
int_list.sort()
for i in int_list[:-4:-1]:
	print(i)