'''
Considering the ClassOne class and the p object, write code on line 11 in order to set the value of the p2
 attribute to 5 for the current instance of the class, without using a function.

'''
'''

class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def square(self, p3):
        print(p3 ** 2)
 
p = ClassOne(1, 2)
 
p.p2 = 5
 
print(p.p2)
'''
d = {"a": 1, "b": 2, "c": 3}
if d.values()<=1:
	print(d)
