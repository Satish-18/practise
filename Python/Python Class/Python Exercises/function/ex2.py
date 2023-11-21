#Implement a function called my_func() that takes a single parameter x (a list) and eliminates
# all duplicates from the list, also returning the result when the function is called.


def my_func(x):
	return list(set(x))

result = my_func([11, 12, 13, 11, 15, 18, 18, 22, 20, 16, 12])
print(result)

