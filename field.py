class Field:
    def __init__(self, size):
        self.size = size

        self.field = str()
    
    # DECORATOR

    def fill(self):
        for row in range(self.size):
            for column in range(self.size):
                self.field += "#"

            self.field += "\n"
            
obj = Field(5)

obj.fill()