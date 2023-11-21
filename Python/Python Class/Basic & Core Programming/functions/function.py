
#Returning  multiple values using function
def calculation(a,b):
	x=a+b
	y=a*b
	z=a-b
	w=a/b
	return x,y,z,w
result=calculation(10,20)
print(result)
for i in result:
	print(i)

#Finding the factorial of number using recursion in function
def factorial(n):
	if n==0:
		result= 1
	else:
		result= n*factorial(n-1)
	return result
print(factorial(5))

#Passing function as a paramater
def dispay(fun):
	return "hello"+fun
def name():
	return "satish"
print(dispay(name()))

#Using function inside a function
def display(name):
	def message():
		return 'Hello '
	result=message()+name
	return result
print(display('Satish subedi!'))

#Passing sequence to function
def display(list):
	for i in list:
		print(i)
display([1,4,3,6])
