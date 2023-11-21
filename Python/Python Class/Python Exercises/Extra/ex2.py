'''Create a script that iterates through text files and checks if strings p, y, t, h, o, or n are found
 in the content of the text file. If any of those strings is found, append that string to a list.
'''
 

import glob
 
letters = []
file_list = glob.iglob("letters/*.txt")
check = "python"
 
for filename in file_list:
    with open(filename,"r") as file:
        letter = file.read().strip("\n")
    if letter in check:
        letters.append(letter)
 
print(letters)



