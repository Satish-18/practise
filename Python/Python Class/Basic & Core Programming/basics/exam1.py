#1 Using for loop print the letter in the string stsrtind with the letter s only
mystring=('Secret agent are super good at staying hidden')
mystring.split()
for word in mystring.split():
	first_letter=word.lower()[0]
	if first_letter=='s':
		print(word)


#2 use a list of comprehension to print first letter of string
mystring=('Secret agent are super good at staying hidden')
mystring.split()
print([words[0] for words in mystring.split()])



#3 print words with even number
mystring=('Secret agent are super good at staying hidden')
mystring.split()
for word in mystring.split():
	if len(word)%2==0:
		print(word)


#4 use comphrension to print even number
print([x for x in range(0,11) if x%2==0])



#5 using range function to print even number
print(list(range(0,11,2)))


#6 use comprehension to creat random number 10
import random
print([random.randint(0,100) for num in range(0,11)])


#7 use for loops to create 10 random number
import random
result=[]
for x in range(0,11):
	result.append(random.randint(0,100))
	print(result)


#8 print even number using while loop until the rea num occurs printing please input a number
result=3
while result%2!=0:
	num=int(input("please enter a number:"))
	if num%2==0:
		resut=2
		print('thank you')