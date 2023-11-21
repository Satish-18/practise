#Instance method
class product:
    def __init__(self):
        self.name="Iphone"
        self.description="It's awasome"
        self.price=700
    def display(self): #calling the methon ie self is use because of that
        print(self.name)
        print(self.description)
        print(self.price)
p1=product()
p1.display()

p2=product()
p2.display()
