
#Considering the code below, write code that prints out True! if the last character
# of the largest (alphabetically) value in the dictionary is n. Otherwise, print out False!

x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"} 
if sorted(x.values())[-1][-1] == "n":
    print("True!")
else:
    print("False!")