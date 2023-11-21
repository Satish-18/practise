#Private accessspecifier
class student:
    def __init__(self):
        self.id=72
        self.name="satish" #Public specifier ie can access directilly by creating the object of it


e=student()
print(e.id)
print(e.name)


#public access specifier
class student:
    def __init__(self):
        self.__id=72
        self.__name="satish" #Pprivatespecifier ie cannot access directilly by creating the object of it
    def display(self):
        print(self.__id)
        print(self.__name)

e=student()
e.display()
#it is name mangling we can use it to access Private element
print(e.__student__id)
