from time import sleep
import msvcrt
from apple import *
from field import *
from snake import *
import os


if __name__ == "__main__":
    pass


_field = Field(10)
_snake = Snake(_field)
_apple = Apple(_field,_snake)

direction = ''

while True:
    sleep(0.5)

    if msvcrt.kbhit():
        direction = format(msvcrt.getch())
    
    _snake.move(direction)

    # _field.show(_field.fill(_snake, _apple))
    
    _field.fill(_snake, _apple)

    os.system("CLS")

    _field.show()


    