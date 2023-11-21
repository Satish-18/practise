#Creating programmer job
class Programmer():
    def setName(self,n):#setter takes two arg
        self.name=n
    def getName(self):#Getter always return self   #takes ane arg
        return sef.name
    def setSalary(self,sal):
        self.salary=sal
    def getSalary(self):
        return self.salary
    def setTechnologies(self,tech):
        self.technologies=tech
    def getTechnologies(self):
        return self.technologies

p1=Programmer()
p1.setName("Satish") #always takes parameter
p1.setSalary(100000)
p1.setTechnologies(["python","Django"])

print(p1.getName) #print passed parameter
print(p1.getSalary)
print(p1.getTechnologies)
