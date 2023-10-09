import math

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
 
def getPrime(n):
    c = 1
    while n > 0:
        c += 1
        if isPrime(c):
            n -= 1
    return c

number = input('Введите подярковый номер простого числа: ')
if number.isdigit():
    print('Простое число с порядковым номером ' + str(number)  + ': ' + str(getPrime(int(number))))
else:
    print('Введён неподходящий тип данных!')