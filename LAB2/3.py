import random as r

size = r.randint(4,6)
matrix = [[r.randint(-5, 15) for j in range(size)] for i in range(size)]

for i in matrix:
	print(i)
for i in range(size):
	sum = 0
	for j in range(size):
		sum += matrix[j][i]
		if matrix[j][i] < 0:
			break
	if matrix[j][i] < 0:
		continue
	print('Сумма ' + str(i+1) + ' столбца: ' + str(sum))