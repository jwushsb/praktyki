import random as rn

class Rng:
    def __init__(self):
        self.nbr = 10

    def gues_nb(self):
        self.nbr = rn.randrange(0, 10)
        return self.nbr

    def shuf(self):
        pass

f = Rng()
print(f.gues_nb())
chs = input("Wybierz numer od ")

