#Write a while loop that prints out the value of x times 10 while x is less than or equal to 4 and then prints
# out Done! when x becomes larger than 4. Be careful not to end up with an infinite loop!

x=0
while(x<=4):
	print(x*10)
	x=x+1
	if x>4:
		print("Work is Done")

