from random import *

class Apple():

    def __init(self,fild,snake):
        self.apple = self.appleSpawn(self,fild,snake)

    def appleSpawn(self,fild,snake):
        
        tmp = list()
        tmp.append([randint(1,fild.WIDTH)],[randint(1,fild.HEIGHT)])

        