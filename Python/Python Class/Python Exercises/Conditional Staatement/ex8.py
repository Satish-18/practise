
#Considering the code below, write code that prints out True! if the value associated with key number
# 5 is Perl or the number of key-value pairs in the dictionary divided by 5 returns a remainder less than 2. Otherwise, 
#print out False!

x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

if x[5] == "Perl" or len(x) % 5 < 2:
    print("True!")
else:
    print("False!")