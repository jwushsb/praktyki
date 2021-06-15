import datetime as dt

class Person:
    def __init__(self, imie, birth_year):  
        self.imie = imie
        self.birth_year = birth_year


    def Hello(self):
        x = dt.datetime.today()
        x = x.year
        print("Witam jestem wesoły ", self.imie, " urodziłem się w ", str(self.birth_year), " roku i mam ", (x - self.birth_year), " lat")
    
    

p1 = Person('Grzegorz', 1992)

print(p1.birth_year)
p1.Hello()


