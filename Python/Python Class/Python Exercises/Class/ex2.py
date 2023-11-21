'''
Considering the ClassOne class and the p object, write code  in order to call the square()
 method for the current instance of the class using 10 as an argument and print the result to the screen.

'''
class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def square(self, p3):
        print(p3 ** 2)

p = ClassOne(1,3)
p.square(10)


