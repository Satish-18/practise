#all the class with all the class as abstract ie interface in python
#Abstraction
from abc import abstractmethod,ABC

class BMW(ABC):
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(selfl):
        pass

    @abstractmethod
    def drive(self):
        pass

class Threeseries(BMW): #inheriting the class BMW
    def __init__(self,cce,make,model,year):
        BMW.__init__(self,make,model,year)
        self.cce=cce

    def display(self):
        print(self.cce) #it can define it's one function ie child calss


    def start(self):
        super().start()
        print("Button start")


    def stop(self):
        super().stop()
        print("Button stop")

    def drive(self):
        print("Threeseries is being driven")


class Fiveseries(BMW): #inheriting the class BMW
    def __init__(self,pae,make,model,year):
        BMW.__init__(self,make,model,year)
        self.pae=pae

    def drive(self):
        print("Fiveseries is being driven")



th=Threeseries(True,"BMW","328i","2028")
print(th.cce)
print(th.make)
print(th.model)
print(th.year)
th.start()
th.stop()
