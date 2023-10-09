import random as r
my_tuple = tuple(r.randint(0,100) for i in range(r.randint(5,10)))

print('Мой кортеж:', my_tuple)
print('Первый элемент:', my_tuple[0])
print('Последний жлемент:', my_tuple[-1])