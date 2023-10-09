import random as r
import msvcrt
import os
import math as m


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(m.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def Task(n):
    if type(n) is list:
        #newList = list(set(n))
        newList = []
        for i in n:
            if i not in newList:
                newList.append(i)
        print('Новые данные:', newList)
        i = 0
        while newList[i] <= 0 and i < len(newList):
            i += 1
        print('Сумма новых данных после первого положительного элемента:', sum(newList[i+1::]))
    elif type(n) is dict:
        print('Первые три наименьших значения:', dict(sorted(n.items(), key=lambda x:x[1])[0:3]))
    elif type(n) is int:
        if isPrime(n):
            print('Число простое!')
        else:
            print('Число составное!')
    elif type(n) is str:
        print('Самое длинное слово: ', sorted(n.split(), key=lambda word: len(word))[-1])

while True:
    #os.system('cls')
    print('Выберите входной тип данных:\n1. Строка\n2. Словарь\n3. Число\n4. Строка\n5. Выход')
    pressedKey = msvcrt.getwch()
    os.system('cls')
    if pressedKey == '1':
        x = [r.randint(-10,10) for i in range(r.randint(10,20))]
    elif pressedKey == '2':
        x = {i:r.randint(0,100) for i in range(r.randint(10,15))}
    elif pressedKey == '3':
        x = r.randint(0,100)
    elif pressedKey == '4':
        x = ''.join(r.choice('abcdef ') for i in range(50))
    elif pressedKey == '5':
        break
    else:
        continue
    print('Входные данные:', x)
    Task(x)
    print('Нажмите любую клавишу чтобы выйти...')
    msvcrt.getwch()
    os.system('cls')
os.system('cls')