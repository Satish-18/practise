#Exception is a class in a python
#we are going to handle zero division error
a,b=[int(x) for x in input("Enter the number:").split()]
c=a/b #stop here if error occur as we can see in output
print(c)
print("After the ececution")


#using try and except block
try:
    a,b=[int(x) for x in input("Enter the number:").split()]
    c=a/b #stop here if error occur as we can see in output
    print(c)
except ZeroDivisionError:
    print("Division by is not allowed")
    print("please enter a non zero number")
print("After the ececution")


#finally block
try:
    f=open("myfile","w")
    a,b=[int(x) for x in input("Enter the number:").split()]
    c=a/b #stop here if error occur as we can see in output
    print(c)
    f.write("writing %d into file"%c)
except ZeroDivisionError:
    print("Division by is not allowed")
    print("please enter a non zero number")
finally:
    f.close()
    print("file closed")
print("After the ececution")


#else--execute only if no exception is raised
try:
    f=open("myfile","w")
    a,b=[int(x) for x in input("Enter the number:").split()]
    c=a/b #stop here if error occur as we can see in output
    f.write("writing %d into file"%c)
except ZeroDivisionError:
    print("Division by is not allowed")
    print("please enter a non zero number")
else:
    print("You have enter a non zero number")
finally:
    f.close()
    print("file closed")
print("After the ececution")
