#Implement a function called my_func() that takes a single parameter x and multiplies it with each
# element of range(5), also adding each multiplication result to a new (initially empty) list called my_new_list.
# Finally, the list should be printed out to the screen after the function is called.




def my_func(x):
    my_new_list = []
    for i in range(5):
        my_new_list.append(i * x)
    return my_new_list
 
result = my_func(2)
print(result)