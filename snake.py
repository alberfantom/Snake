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
        
        if side == 'w':
            self.snake[0][1] -= 1
        elif side == 's':
            self.snake[0][1] += 1
        elif side == 'a':
            self.snake[0][0] -= 1
        elif side == 'd':
            self.snake[0][0] += 1



