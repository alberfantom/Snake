from random import *

class Apple():

    def __init__(self,fild,snake):
        self.apple = self.appleSpawn(fild,snake)

    def appleSpawn(self,fild,snake):
        
        tmp = list()
        tmp.append([randint(1,fild.size),randint(1,fild.size)])



        return tmp

        