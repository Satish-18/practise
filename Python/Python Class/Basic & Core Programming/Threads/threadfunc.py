#creating a thread using a function

from  threading import Thread

def displayNumbers():
    i=0
    while(i<=10):
        print(i)
        i+=1

t=Thread(target=displayNumbers)
t.start()

#printing thread name
from threading import *
def displayNumbers():
    i=0
    while(i<=10):
        print(i)
        i+=1
print(current_thread().getName())
t=Thread(target=displayNumbers)
t.start()

#Extending the thread and override
from threading import Thread
class myThread(Thread):
    def run(self):
        i=0
        while(i<=10):
            print(i)
            i+=1

t=myThread()
t.start()
