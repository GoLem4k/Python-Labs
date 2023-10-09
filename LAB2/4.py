def getSquare(a):
    return a*a

while True:
    try:
        print('Квадрат числа:', getSquare(int(input('Число: '))))
    except ValueError:
        print('Получена ошибка - ValueError')
    finally:
        print('Код отработал')