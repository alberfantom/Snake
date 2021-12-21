from random import *

class Apple():
    def __init__(self, _field, _snake):      
        self.spawn_apple(_field, _snake)

    def spawn_apple(self, _field, _snake):
        self.coord = [randint(1, _field.size - 2), randint(1, _field.size - 2)]
        
        if self.coord in _snake.coords:
            self.spawn_apple(_field, _snake)