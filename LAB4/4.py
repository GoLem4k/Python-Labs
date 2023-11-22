import math

class Cup:
    cup_amount = 0
    def __init__(self, color, volume):
        self.color = color
        self.volume = volume
        Cup.cup_amount += 1
    def displayInfo(self):
        print(f"Цвет: {self.color}, Объём: {self.volume}")

    @staticmethod
    def calculateVolume(radius, height):
        return int(math.pi * radius * radius * height)
    
    @classmethod
    def getCupAmount(cls):
        return cls.cup_amount

cup1 = Cup("Gray", 300)
cup2 = Cup("White", 400)

cup1.displayInfo()
cup2.displayInfo()

print(Cup.calculateVolume(3, 10))
print(f"Количество кружек: {Cup.getCupAmount()}")