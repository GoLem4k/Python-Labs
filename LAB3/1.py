import os

with open('F1.txt', 'w+') as fileF1:

    textByUser = 0

    while textByUser is not '':
        textByUser = input("Введите текст: ");
        fileF1.write(textByUser + '\n')

    fileF1.seek(0)
    linesF1 = fileF1.readlines()

    with open('F2.txt', 'w+') as fileF2:
        for line in linesF1:
            if not any(char.isdigit() for char in line):
                fileF2.write(line)
        
        counter = 0
        fileF2.seek(0)
        linesF2 = fileF2.readlines()
        for line in linesF2:
            if line[0] == 'F':
                counter += 1

print('Количество строк, начинающихся на "F":', counter)