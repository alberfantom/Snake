from tkinter import *

class Application():
    def __init__(self, WIDTH, HEIGHT):
        self.root = Tk()

        self.width = WIDTH
        self.height = HEIGHT

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    Application(800, 600).run()