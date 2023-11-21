#Cubes of number<<< by basic way
list=[]
for x in range(1,10):
    list.append(x**3)
print(list)


#Cubes of number<<< by list comphrehension
list=[]
list=[x**3 for x in range(1,11)]
print(list)

#Even number in a list
list=[]
list=[x for x in range(2,21) if x%2==0]
print(list)

#product of element in two different list
a=[1,2,3,4,5]
b=[6,7,8,9,10]
z=[]
z=[a[i]*b[i] for i in range(len(a))]
print(z)


#Find common element in list
a=[2,4,6,8]
b=[1,2,3,4]
c=[i for i in a if i in b]
print(c)
