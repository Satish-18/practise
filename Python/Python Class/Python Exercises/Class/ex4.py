'''
Considering the ClassOne class and the p object, write code on lines 11 and 12 in order to set the value of the p2
 attribute to 50 for the current instance of the class using a function, and then get the new value of p2, 
 again using a function, and print it out to the screen as well.

'''

class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def square(self, p3):
        print(p3 ** 2)

p = ClassOne(1, 2)

#setter,getter and hasattribute attribute 
setattr(p,'p2',50)
print(getattr(p,'p2'))
print(hasattr(p,'p2'))