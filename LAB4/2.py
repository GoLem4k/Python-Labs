class City():
    def getTravelPrice(self, price):
        return self.distance * price
    
    def getTravelTime(self, speed):
        return self.distance / speed

    def __init__(self, name, distance):
        self.name = name
        self.distance = distance

class Transport():
    transports_amount = 0

    @classmethod
    def getTransportAmount(cls):
        return cls.transports_amount

    def methodOfTransportation():
        print('Способо передвижения: None')
        

class Plane(Transport):

    def __init__(self):
        self.name = 'Самолёт'
        self.speed = 800
        self.price = 5
        Transport.transports_amount += 1

    def methodOfTransportation(self):
        print('Способ передвижения: Самолёт')

class Train(Transport):
    
    def __init__(self):
        self.name = 'Поезд'
        self.speed = 160
        self.price = 4
        Transport.transports_amount += 1

    def methodOfTransportation(self):
        print('Способ передвижения: Поезд')

class Auto(Transport):

    def __init__(self):
        self.name = 'Автомобиль'
        self.speed = 80
        self.price = 2
        Transport.transports_amount += 1

    def methodOfTransportation(self):
        print('Способ передвижения: Автомобиль')

cities = [City('Италия:', 900), City('Польша:', 600), City('Россия:', 400)]

transports = [Plane(), Train(), Auto()]

with open("travels.txt", "w") as fileTravels:
    min_prize = None;
    for transport in transports:
        transport.methodOfTransportation()
        for city in cities:
            tp = city.getTravelPrice(transport.price)
            min_prize = tp if (min_prize == None) else tp if (tp < min_prize) else min_prize
            print(city.name, 'расстояние -', city.distance, 'цена -', tp, 'время поездки -', city.getTravelTime(transport.speed))
            fileTravels.write(city.name + ' расстояние - ' + str(city.distance) + ' цена - ' + str(tp) + ' время поездки - ' + str(city.getTravelTime(transport.speed)) + "\n")
print(f"Лучшая цена: {min_prize}")
print(f"Количество транспортных средств: {Auto.getTransportAmount()}")