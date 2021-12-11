#import time
import msvcrt
from apple import Apple
from field import *
from snake import *


if __name__ == "__main__":
    pass


_field = Field(10,10)
_apple = Apple(_field)
_snake = Snake(_field)


direction = ''
while 1:
    #time.sleep(1)
    if msvcrt.kbhit():
        direction = format(msvcrt.getch())
    
    _snake.move(_snake,direction)


    