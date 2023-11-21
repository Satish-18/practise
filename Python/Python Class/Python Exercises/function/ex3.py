#Implement a function called my_func() that takes a single parameter x (a tuple) and for each element of the
# tuple that is greater than 4 it raises that element to the power of 2, also adding it to a new (initially empty) list called
# my_new_list. Finally, the code returns the result when the function is called.

def my_func(x):
	my_new_tuple=[]
	for i in x:
		if i>4:
			my_new_tuple.append(i**2)
	return my_new_tuple

result = my_func((2, 3, 5, 6, 4, 8, 9))
print(result)


