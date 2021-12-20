from random import *
import main

class Apple():
    def __init__(self):
        self.spawn_apple()
        
    def spawn_apple(self):
        self.coord = [randint(1, main.field.size - 1), randint(1, main.field.size - 1)]
        
        if self.coord in main.snake.coords:
            self.spawn_apple()