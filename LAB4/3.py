class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
class Door:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Room:

    doors = []
    windows = []
    def __init__(self, length, width, height, doors = None, windows = None):
        self.length = length
        self.width = width
        self.height = height
        self.doors = doors.copy() if doors != None else []
        self.windows = windows.copy() if windows != None else []
    def getGluingArea(self):
        gluing_area = (self.length + self.width) * 2 * self.height
        for door in self.doors:
            gluing_area -= door.width * door.height
        for window in self.windows:
            gluing_area -= window.width * window.height
        return gluing_area

myRoom = Room(3,5,4, [Door(1,2)], [Window(1,1), Window(2,2)])

print(myRoom.getGluingArea())