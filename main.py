from tkinter import *

class Application():
    def __init__(self, WIDTH, HEIGHT):
        self.width = WIDTH
        self.height = HEIGHT

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    Application(1,2)