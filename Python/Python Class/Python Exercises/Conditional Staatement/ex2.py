#print true if any one condition of is true, string contains character  z and y apperar twice in the string

x = "The days of Python 2 are almost over. Python 3 is the king now."

if "z" in x or x.count("y")==2:
	print('true!')