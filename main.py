import time
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

start_time_show = time.time()
start_time_move = time.time()
while True:
    

    if msvcrt.kbhit():
        direction = format(msvcrt.getch())

    if (time.time() - start_time_move) > 0.3:
        start_time_move = time.time()
        _snake.move(direction)
    
    if (time.time() - start_time_show) > 0.3:
        start_time_show = time.time()
        
        # print("\n" * 2)
        os.system("CLS") 

        _field.fill(_snake, _apple)
        _field.show()