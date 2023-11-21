
#Considering the code below, write code that prints out True! if the sum of all the keys in the dictionary is less 
#than the number of characters of the string obtained by concatenating the values associated with the first 5 keys in the dictionary.
# Otherwise, print out False!

x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"} 

if sum(x) < len(x[1] + x[2] + x[3] + x[4] + x[5]):
    print("True!")
else:
    print("False!")