#overriding implimentation


class BMW:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def start(self):
        print("Start the car")
    def stop(selfl):
        print("Stop the car")

class Threeseries(BMW): #inheriting the class BMW
    def __init__(self,cce,make,model,year):
        BMW.__init__(self,make,model,year)
        self.cce=cce
    def display(self):
        print(self.cce) #it can define it's one function ie child calss

    def start(self):
        print("Button start")  #OVERRIDING
class Fiveseries(BMW): #inheriting the class BMW
    def __init__(self,pae,make,model,year):
        BMW.__init__(self,make,model,year)
        self.pae=pae

    def display(self): #defining function of the class
        print(self.pae)



th=Threeseries(True,"BMW","328i","2028")
print(th.cce)
print(th.make)
print(th.model)
print(th.year)
th.start()
th.stop()
th.display()

#In output we have overridden the functionality avialable in the parent class by implementing the method with the same name but different functionality
#ie overriding
