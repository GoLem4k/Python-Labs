pi4 = 0
num = 1;
for i in range(500):
	if i % 2 == 0:
		pi4 += 1/num
	else:
		pi4 -= 1/num
	num += 2
print('PI:', pi4*4)