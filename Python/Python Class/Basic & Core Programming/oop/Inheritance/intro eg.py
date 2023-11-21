#implimenting BMW system
class BMW:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

class Threeseries(BMW): #inheriting the class BMW
    def __init__(self,cce,make,model,year):
        BMW.__init__(self,make,model,year)
        self.cce=cce


class Fiveseries(BMW): #inheriting the class BMW
    def __init__(self,pae,make,model,year):
        BMW.__init__(self,make,model,year)
        self.pae=pae



th=Threeseries(True,"BMW","328i","2028")
print(th.cce)
print(th.make)
print(th.model)
print(th.year)

sav=Fiveseries(False,"farari","328i","2028")
print(sav.pae)
print(sav.make)
print(sav.model)
print(sav.year)
