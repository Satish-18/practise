'''
Write a class called ClassOne starting on line 1 containing:

The __init__ method with two parameters p1 and p2. Define the corresponding attributes 

inside the __init__ method.

A method called square that takes one parameter p3 and prints out the value of p3 squared.

'''

class ClassOne(object):
	"""docstring for ClassName"""
	def __init__(self, p1,p2):
		self.p1 = p1
		self.p2 = p2

		def square(self,p3):
			print(p3**2)

p = ClassOne(1,2)
print(type(p))
print(p.p1)


class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def square(self, p3):
        print(p3 ** 2)

p = ClassOne(1, 2)
p.square(10)