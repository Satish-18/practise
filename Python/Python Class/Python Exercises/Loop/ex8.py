#Write a while loop that prints out the value of x times y while x is greater than or equal to 5 and less than 10,
# and prints out the result of x divided by y when x becomes 10. Be careful not to end up with an infinite loop!

x=5
y=2
while(x>=5 and x<10):
	print(x*y)
	x=x+1
if(x==10):
	print(x/y) 


