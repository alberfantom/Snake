#import time
import msvcrt
from apple import *
from field import *
from snake import *


if __name__ == "__main__":
    pass


_field = Field(10)
_snake = Snake(_field)
_apple = Apple(_field,_snake)


direction = ''
while 1:
    #time.sleep(1)
    if msvcrt.kbhit():
        direction = format(msvcrt.getch())
    
    _snake.move(direction)
    _field.fill(_snake,_apple)
    print(_field.field)


    