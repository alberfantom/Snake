import main

class Snake():
    def __init__(self):
        self.coords = list()
        self.coords.append([main.field.size // 2, main.field.size // 2])

    def move(self, side, apple, field):
        self.apple = apple

        i = len(self.coords) - 1
        while i > 0:
            self.coords[i] = self.coords[i - 1]

            i -= 1

        if not self.is_collision_border():
            if side == "w":
                self.coords[0][0] -= 1

            elif side == "s":
                self.coords[0][0] += 1

            elif side == "a":
                self.coords[0][1] -= 1

            elif side == "d":
                self.coords[0][1] += 1

    def is_collision_border(self):
        coord = self.coords[0]

        # Правая и левая граница
        # Верхняя и нижняя граница
        if coord[0] == 0 or coord[0] == 10 \
            or coord[1] == 0 or coord[1] == 10:
                return True
        
        return False
    
    def is_collision_apple(self):
        if self.apple.coord == self.coords[0]:
            self.coords.append([self.coords[-1][0], self.coords[-1][0]])

            self.apple.spawn_apple(self, self.field)

    def is_collision_snake(self):
        pass
