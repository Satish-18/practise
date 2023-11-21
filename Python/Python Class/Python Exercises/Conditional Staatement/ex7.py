#Considering the code below, write code that prints out True! if 115 appears at least 
#once inside the list or if it is the first element in the list. Otherwise, print out False!

x = [115, 115.9, 116.01, 109, 115, 119.5, ["length", "width", "height"]]

if x.count(115) >= 1 or x.index(115) == 0:
    print("True!")
else:
    print("False!")