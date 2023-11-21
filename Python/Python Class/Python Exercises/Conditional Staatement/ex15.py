#Considering the code below, write code that prints out True! if the last element of the first range is greater than 3,
# prints out False! if the last element of the second range is less than 9, and prints out None! otherwise.

x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]

if x[0][-1] > 3:
    print("True!")
elif x[1][-1] < 9:
    print("False!")
else:
    print("None!")
