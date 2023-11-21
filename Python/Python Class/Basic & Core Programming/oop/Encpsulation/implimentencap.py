#implimenting encapsulation using setter and getter
class student():
    def setId(self,id):
        self.id=id
    def getId(self):
        return self.id
    def setName(self,name):
        self.name=name
    def getNme(self):
        return self.name


s=student()
s.setId(72)
s.setName("satish subedi")
print(s.getId())
print(s.getNme())
