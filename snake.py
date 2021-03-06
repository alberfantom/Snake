class Snake():
    def __init__(self, _field):
        self.coords = list()
        self.coords.append([_field.size // 2, _field.size // 2])

    def move(self, side, _field, _apple):
        if not self.is_collision_border(_field) \
            and not self.is_collision_snake():
                if len(self.coords) != 1:
                    i = len(self.coords) - 1

                    while i > 0: 
                        self.coords[i][0] = self.coords[i - 1][0]
                        self.coords[i][1] = self.coords[i - 1][1]

                        i -= 1

                coord_basic = [self.coords[-1][0], self.coords[-1][1]]
                
                if side == "w":
                    self.coords[0][1] -= 1

                elif side == "s":
                    self.coords[0][1] += 1

                elif side == "a":
                    self.coords[0][0] -= 1

                elif side == "d":
                    self.coords[0][0] += 1
                    
                if self.is_collision_apple(_apple):
                    self.coords.append(coord_basic)

                    _apple.spawn_apple(_field, self)

    def is_collision_border(self, _field):
        coord = self.coords[0]

        # Правая и левая граница
        # Верхняя и нижняя граница
        if coord[0] == 0 or coord[0] == _field.size - 1\
            or coord[1] == 0 or coord[1] == _field.size - 1:
                return True
        
        return False

    def is_collision_apple(self, _apple):
        if _apple.coord == self.coords[0]:
            return True

        return False

    def is_collision_snake(self):
        if len(self.coords) != 1:
            print(self.coords)

            if self.coords[0] in self.coords[1:]:
                return True

            return False