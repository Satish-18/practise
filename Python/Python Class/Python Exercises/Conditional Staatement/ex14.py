
#Considering the code below, write code that prints out True! if the 3rd element of the 3rd range
# is less than 6, prints out False! if the 1st element of the second range is 5, and prints out None! otherwise.

x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]

if x[2][2] < 6:
    print("True!")
elif x[1][0] == 5:
    print("False!")
else:
    print("None!")