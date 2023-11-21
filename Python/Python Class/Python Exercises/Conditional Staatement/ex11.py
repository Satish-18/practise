#Considering the code below, write code that prints out True! if the largest key in the 
#dictionary divided by the second largest key in the dictionary returns a remainder equal to the smallest key in the dictionary. 
#Otherwise, print out False!

x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

if sorted(x.keys())[-1] % sorted(x.keys())[-2] == sorted(x.keys())[0]:
	print("True")
else:
	print("False")