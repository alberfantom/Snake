from field import *

class Snake():
    
    def __init__(self,fild):

        self.coords = list()
        self.coords.append([fild.size/2,fild.size/2])

    def move(self,side):

        i = len(self.coords) - 1
        while i > 0:
            self.coords[i] = self.coords[i - 1]

            i -= 1
        
        if side == "b'w'":
            self.coords[0][1] -= 1
        elif side == "b's'":
            self.coords[0][1] += 1
        elif side == "b'a'":
            self.coords[0][0] -= 1
        elif side == "b'd'":
            self.coords[0][0] += 1



