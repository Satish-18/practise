#Write a for loop that iterates over the x list and prints out all the elements of the list in reversed order and multiplied by 10.

x = [10, 12, 13, 14, 17, 19, 21, 22, 25]

for i in sorted(x,reverse=True):
	print(i*10)
