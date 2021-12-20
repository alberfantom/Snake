import time
import msvcrt

import field
import snake
import apple

direction = ""

start_time_move = time.time()

_field = field.Field(25)
_snake = snake.Snake(_field)
_apple = apple.Apple(_field, _snake)

while True:
    if msvcrt.kbhit():
        direction = format(msvcrt.getch().decode())

    if (time.time() - start_time_move) > 0.3:
        start_time_move = time.time()
        _snake.move(direction, _field)
        _field.fill(_snake, _apple)
        _field.show()
   

        