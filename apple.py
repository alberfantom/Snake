from random import *

class Apple():
    def __init__(self, field, snake):
        self.spawn_apple(snake, field)
        
    def spawn_apple(self, snake, field):
        self.coord = [randint(1, field.size), randint(1, field.size)]
        
        if self.coord in snake.coords:
            self.spawn_apple()
