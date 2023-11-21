
#Considering the code below, write code that prints out True! if the 3rd element of the first range is less than 2, 
#prints out False! if the 5th element of the first range is 5, and prints out None! otherwise.

x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]

if x[0][2] < 2:
    print("True!")
elif x[0][4] == 5:
    print("False!")
else:
    print("None!")