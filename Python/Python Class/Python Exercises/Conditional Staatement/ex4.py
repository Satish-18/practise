#write the code that print out  True, if the second string of the first list in  x ends with the letter h and 
# the first string of the second list in x also ends with letter h , and print out False otherwise

x = [115, 115.9, 116.01, ["length", "width", "height"], 109, 115, 119.5, ["length", "width", "height"]]

if x[3][1].endswith("h") and x[7][0].endswith("h"):
    print("True!")
else:
    print("False!")