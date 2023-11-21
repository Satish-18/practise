#STRING
name='satish subedi'
print(name.split('s'))#by split method we can remove the certain string from the given string and split

user_name='subedi'
action='playing cricket'
print('satish {} is {}'.format(user_name,action))#just like concatination





#LIST->>it is am unorder set of element in square bracket it is mutuable
list=[1,4,5,6,'satish']
print(len(list))#it returns the length
print(list)
list.append(4)#adding new element
print(list)
list.pop(4)#deleting indexing element
print(list)
print(list[0])#indexing
list[2]='welcome to python'#adding new element in indexing element by removing previous element
print(list)
my_list=[1,7,5,9]
my_list.reverse()#print in reverse order
print(my_list)
my_list.sort()#print is sorted order
print(my_list)
my_list.insert(0,'new')#placing new element in place of previous eement
print(my_list)




#SETS->>is also unordered list of items in curly braces
x=set()
x.add(1)#jist adding element to null sets
print(x)
x.add(2)
print(x)
my_list={1,1,1,1,1,5,5,6,7,8,8,7,6,5,5,4,3,3,2,2,1}#it is uniqur
print(my_list)




#DICTONARIES->>it contains key values it is also mutuable
dict={'name':'satish subedi','age':20}
print(dict['name'])
print(dict.items())
print(dict.values())



#TUPLES->>they are immutable inside pranthesis
tup=(1,2,3,'satish')
print(tup)
t=(1,4,6,1,1)
print(t.index(6))#show thw indexing of element
print(t.count(1))#count the repeatation of element


