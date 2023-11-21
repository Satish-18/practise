class Student():
    major='CSE'#difining static field name as major globally
    def __init__(self,rollno,name):
        self.rollno=name
        self.name=name

s1=Student(1,"satish")
s2=Student(2,"swostika")
print(s1.major)
print(s2.major)
print(s1.name)
print(s2.name)
print(Student.major)


#Defining method and field to count the no of class that are created and display the count
class objectcounter():
    numberofobjects=0 #static field
    def __init__(self):
        objectcounter.numberofobjects+=1 #to increment the 1 every time init is invoked
    @staticmethod
    def displaycount():
        print(objectcounter.numberofobjects)

o1=objectcounter()
o2=objectcounter()

objectcounter.displaycount()


###,,.,......creating inner class
#creat class car having inner class engine

class car():
    def __init__(self,make,year):
        self.make=make
        self.year=year
    class engine():
        def __init__(self,number):
            self.number=number
        def start(self): #method
            print("engine started")


c=car("lamborgini",2028)
e=c.engine(123)
e.start() #accesing method
