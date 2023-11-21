'''
Considering the ClassOne class, write code starting on line 9 to create a child class called ClassTwo
 that inherits from ClassOne and also has its own method called times10() that takes a single parameter x
  and prints out the result of multiplying x by 10.


'''


class ClassOne:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def square(self, p3):
        print(p3 ** 2)

class ClassTwo(ClassOne):
	
		def times10(self,x):
			print(x*10)
		
k = ClassTwo(3,4)
s=k.times10(3)
