#REDUCED
#Find sum of every element in a list
from functools import reduce
li=[10,14,15,17]
h=reduce(lambda x,y:x+y,li)
print(h)
