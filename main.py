import time
import msvcrt

import field
import snake
import apple

direction = ""

start_time_move = time.time()

_field = field.Field(int(input("Введите размер поля: ")))
_snake = snake.Snake(_field)
_apple = apple.Apple(_field, _snake)

FPS = 2.5

while True:
    if msvcrt.kbhit():
        direction = format(msvcrt.getch().decode())

    start_time_move = time.time()

    _snake.move(direction, _field, _apple)

    _field.fill(_snake, _apple)
    _field.show()

    time.sleep(1 / FPS)
        