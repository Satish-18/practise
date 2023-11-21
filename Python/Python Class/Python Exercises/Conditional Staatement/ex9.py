
#Considering the code below, write code that prints out True! if 3 is a key in the dictionary and the smallest
# value (alphabetically) in the dictionary is C#. Otherwise, print out False!

x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"} 

if 3 in x and sorted(x.values())[0] == "C#":
    print("True!")
else:
    print("False!")