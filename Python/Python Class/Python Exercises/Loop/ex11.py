#Write code that will iterate over the x and y lists and multiply each element of x with each element of y that is less than
#or equal to 10, also printing the results to the screen. For y's elements that are greater than 10, multiply each element of
 #x with y squared.

x = [2, 4, 6, 8]
y = [5, 10, 15, 20]
 
for i in x:
    for j in y:
        if j <= 10:
            print(i * j)
        else:
            print(i * j ** 2)	
