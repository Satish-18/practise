'''
LAMDBA:--Anonymous function
SYNTAX:lambda arg_list:expression

'''
#Calculating cube of a number using lamda
s=lambda n:n**3
print(s(2))

#Calculating the sum
a=lambda x,y:x+y
print(a(10,20))

#calculating odd and even and return result
t=lambda x:'yes'if x%2==0 else 'no'
print(t(10))
