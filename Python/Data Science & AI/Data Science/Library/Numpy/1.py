
import numpy as np
import random

arr = np.arange(50).reshape(5,10)
print(arr[1:4,1:6])


'''
Array with array
Array with scalar 
Universal array function
'''

arr = np.arange(1,11)
print(arr+100)


'''
Exercises

'''

#create an array of 10 zeros
print(np.zeros(10))

#crate an array of 10 ones
print(np.ones(10))

#create an array of 10 fives
print(np.zeros(10)+5)

#create an array of integers from 10 to 50
inte = np.arange(10,51)
print(inte)

#create an array of even integers from 10 to 50
even = np.arange(10,51,2)
print(even) 

#create a 3*3 matrix value ranging from 0-8
inte = np.arange(0,9).reshape(3,3)
print(inte) 

#create 3*3 identity matrix
arr_2d = np.identity(3)
print(arr_2d)

#create a random number between 0-1
inte = np.random.rand(1)
print(inte)


#use numpy to generate array of random numbers 
#sampled from a standard normal distribution
print(np.random.rand(25))


#creae the matrix
arrange = np.arange(1,101).reshape(10,10)/100
print(arrange)

#create a array of lineraly space points between 0=1
print(np.linspace(0,1,20))

