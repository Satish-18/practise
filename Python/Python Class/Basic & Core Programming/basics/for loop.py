#FOR LOOPS->>Iteration or repeatation of group


#Printing verticaly
my_list=[1,3,5,6,7]
for items in my_list:
	print(items)


#Printing horizontally
my_list=[1,3,5,6,7]
for items in my_list:
	print(items,end=' ')

#examples
for letter in'this is python':
	print('hello')  #print hello in place of every string in iterable lists.
	print('\n')



#TUPES UNPACKING
my_list=[(1,2),(3,4),(5,6)]
for item1,item2 in my_list:
	print(item1)   #print the single number of iterable list
	print(item2)
	print('\n')


#For Loops in dictonaries	

d={'k':1,'k2':5,'k3':7}
for items in d:
	print(items)  #print in random order
for keys in d:
	print(keys)   #also in random order


#PYTHON OPERATORS
for num in range(0,11):
    print(num)
print(list(range(0,11))) #Printing the number in the list

####->>use of enumeration
for index,letter in enumerate('abcs'):
	print('at index {} the letter is {}'.format(index,letter))




###ZIP
list1=[1,3,4,5,6]
list2=[7,9,8,6,5]        ###print in pair
for items in zip(list1,list2):
	print(items)




####  MIN &  MAX
pt=[12,67,33,64,78]
print(min(pt))    #Returns min value
print(max(pt))    #Returns max value

'''
LIST OF COMPHREHENSION
>>>unique way of creating list with python

'''

#exampe
mylist=[]
s='somethimg'
for letter in s:
	mylist.append(letter)  #print single letter of the string
	print(letter)

##
s='something'
newlist=[letter for letter in s]##print the list of letter of the string
print(newlist)
###


from random import randint
print(randint(0,100))##creat single random number