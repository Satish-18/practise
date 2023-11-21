#Implement a function called my_func() that takes two default parameters x (a list) and y (an integer),
# and returns the element in x positioned at index y, also printing the result to the screen when called.


def my_func(x, y):
    return x[y]
 
result = my_func(list(range(2,25,2)), 4)
print(result)