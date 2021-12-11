class Field:
    def __init__(self, size):
        self.size = size

        self.field = str()
    
    def fill(self, _snake, _apple):
        for row in range(self.size):
            for column in range(self.size):
                if [row, column] in _apple.coord:
                    self.field += "$"

                elif [row, column] in _snake.coords:
                    self.field += "@"

                else:
                    self.field += "#" 

            if row != self.size - 1:
                self.field += "\n"

    def show(self):
        print("-" * 5)

        print(self.field)

        print("-" * 5)