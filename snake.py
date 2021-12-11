from field import *

class Snake():
    
    def __init__(self,fild):

        self.snake = list()
        self.snake.append([fild.WIDTH/2,fild.HEIGHT/2])

    def move(self,side):

        i = len(self.snake) - 1
        while i > 0:
            self.snake[i] = self.snake[i - 1]

            i -= 1
        
        if side == "b'w'":
            self.snake[0][1] -= 1
        elif side == "b's'":
            self.snake[0][1] += 1
        elif side == "b'a'":
            self.snake[0][0] -= 1
        elif side == "b'd'":
            self.snake[0][0] += 1



