glas = 'уеыаоэяию'
sogl = 'йцкнгшщзхъфвпрлджчсмтьб'
g_count = 0
s_count = 0
spaces = 0
glas_text = ''

my_text = input("Enter your text: ")
for i in my_text:
	if i in glas:
		g_count += 1
		glas_text += i
	elif i in sogl:
		s_count += 1
	elif i == ' ':
		spaces += 1
if g_count == s_count:
	print(glas_text)
print('Количество слов:',spaces+1)