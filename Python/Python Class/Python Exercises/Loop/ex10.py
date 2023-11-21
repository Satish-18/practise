#Write code that will iterate over the x and y lists and multiply each element of x with each element of y
# that is less than 12, also printing the results to the screen.

x = [2, 4, 6, 8]
y = [5, 10, 15, 20]
 
for i in x:
    for j in y:
        if j < 12:
            print(i * j)
