class Field:
    def __init__(self, size):
        self.size = size

    def fill(self, _snake, _apple):
        self.field = str()

        print("\n") # Отделение от другого поля

        # Верхняя граница
        self.field += f" #{'#' * (self.size - 1)}\n"

        for row in range(self.size):
            # Левый край
            self.field += "#"   

            # Содержимое
            for column in range(self.size):
                if [row, column] in _snake.coords:
                    self.field += "@"

                elif _apple.coord[0] == row and _apple.coord[1] == column:
                    self.field += "$"

                else:
                    self.field += "." 
            
            # Правый край
            self.field += "#"

            self.field += "\n"

        # Нижняя граница
        self.field += f" #{'#' * (self.size - 1)}\n"

    def show(self):
        print(self.field, end="")