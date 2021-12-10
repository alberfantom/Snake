class Field():
    def __init__(self, WIDTH, HEIGHT):
        self.field = list()

        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        for row in range(WIDTH):
            for column in range(HEIGHT):
                pass