'''
SYNTAX:
   clas name of a class():
   def_init_(self,par1,par2):
   self.par1=par1
   self.parpar2=par2


   def some_method(self):
   # peform some action
   print(self.par)
   '''

#Passing same parameter
class product:
    def __init__(self):
        self.name="Iphone"
        self.description="It's awasome"
        self.price=700
p1=product()

print(p1.name)
print(p1.description)
print(p1.price)

#Parameterize constructor passng different Parameter
class course():#class
    def __init__(self,name,ratings):#constructor
        self.name=name
        self.ratings=ratings

c1=course("My name is khan",[1,2,3,4,5])
print(c1.name)
print(c1.ratings)

c2=course("Devdas",[6,7,8,9])#objects in python
print(c2.name)
print(c2.ratings)

#instance method to calculate average rating of course
class course:#class
    def __init__(self,name,ratings):#constructor
        self.name=name
        self.ratings=ratings


    def average(self):
        numberofratings=len(self.ratings)
        average=sum(self.ratings)/numberofratings
        print("Average ratings for",self.name, "is",average)

c1=course("My name is khan",[1,2,3,4,5])
print(c1.name)
print(c1.ratings)
c1.average()

c2=course("Devdas",[6,7,8,9])#objects in python
print(c2.name)
print(c2.ratings)
c2.average()
