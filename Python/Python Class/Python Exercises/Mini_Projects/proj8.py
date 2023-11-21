#number gussing game


import random  
 
print("	Hello, What is your name?")
name = input()

print("well, '+ name +', iam thinking of aa number between 1-20")
sectretniumber  = random.randint(2,20)

for gusstaken in range(1,7):
	print('Take the guss')
	guss = int(input())


	if guss <sectretniumber:
		print('Your guss is too low')
	elif guss>sectretniumber:
		print('Your guss is too high')
	else:
		break


if guss == sectretniumber:
	print("god job,'+ name +', your guss my number in '+ str(gusstaken) +',times")
else:
	print('Nope you are wrong  i was thinkking the number' + str(sectretniumber))