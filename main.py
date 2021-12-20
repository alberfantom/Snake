import time
import msvcrt

import field
import snake
import apple

field = field.Field(12)
snake = snake.Snake()
apple = apple.Apple()

direction = ""

start_time_move = time.time()
while True:
    if msvcrt.kbhit():
        direction = format(msvcrt.getch().decode())

    if (time.time() - start_time_move) > 0.3:
        start_time_move = time.time()
        snake.move(direction)
        field.fill()
        field.show()
   

        