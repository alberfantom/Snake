class Field:
    def __init__(self, size):
        self.size = size

        self.field = str()
    
    def fill(self, _snake, _apple):
        for row in range(self.size):
            for column in range(self.size):
                if [row, column] in _apple.coord:
                    self.field += "$"

                elif [row, column] in _snake:
                    self.field += "@"

                else:
                    self.field += "#" 

            self.field += "\n"