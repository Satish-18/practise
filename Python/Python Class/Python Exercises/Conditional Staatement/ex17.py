#Considering the code below, write code that prints out True! if the sum of all the elements of the first range is greater
# than the sum of all the elements of the third range, prints out False! if the largest element of the second range is 
#greater than the largest element of the third range, and prints out None! otherwise.

x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]

 
if sum(x[0]) > sum(x[2]):
    print("True!")
elif max(x[1]) > max(x[2]):
    print("False!")
else:
    print("None!")