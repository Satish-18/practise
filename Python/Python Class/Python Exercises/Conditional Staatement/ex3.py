#Print true if len of x is greater or eqals to 8 and 6th element of the given list  is a float number

x = [115, 115.9, 116.01, ["length", "width", "height"], 109, 115, 119.5, ["length", "width", "height"]] 

if len(x) >= 8 and type(x[6]) is float:
    print("True!")
else:
    print("False!")