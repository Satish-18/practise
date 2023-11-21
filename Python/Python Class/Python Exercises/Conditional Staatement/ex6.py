#Considering the code below, write code that prints out True! if the largest value among the first 3 elements of 
#the list is less than or equal to the smallest value among the next 3 elements of the list. Otherwise, print out False!

x = [115, 115.9, 116.01, 109, 115, 119.5, ["length", "width", "height"]]

if max(x[:3]) <= min(x[3:6]):
    print("True!")
else:
    print("False!")