from field import *

class Snake():
    def __init__(self, field):
        self.coords = list()
        self.coords.append([field.size // 2, field.size // 2])

    def move(self, side, apple,field):
        if apple.coord == self.coords[0]:
            self.coords.append(self.coords[len(self.coords) - 1])
            apple.spawn_apple(self,field)


        i = len(self.coords) - 1
        while i > 0:
            self.coords[i] = self.coords[i - 1]

            i -= 1
        
        if side == "w":
            self.coords[0][0] -= 1

        elif side == "s":
            self.coords[0][0] += 1

        elif side == "a":
            self.coords[0][1] -= 1

        elif side == "d":
            self.coords[0][1] += 1



