#calltalk methon can invoke any method in the object
class duck:
    def talk(self):
        print("Quak Quak")
class human:
    def talk(self):
        print("Hello")

def callTalk(obj):
        obj.talk(); #Dinamecally invokes the talk method

d=duck()
callTalk(d)

h=human()
callTalk(h)


#Ducktyping for independency
class flight:
    def __init__(self,engine):
        self.engine=engine

    def startengine(self):
        self.engine.start(); #Dependency enjection

class airbusengine:
    def start(self):
        print("starting airbus engine")

class boingengine:
    def start(self):
        print("starting boaing engine")

ae=airbusengine()
f=flight(ae)
f.startengine()

be=boingengine()
f1=flight(be)
f1.startengine()
