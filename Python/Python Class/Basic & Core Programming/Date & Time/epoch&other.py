'''
  epoch-->>Start of time==jan 1st 1970
  ctime()==time

'''

import time,datetime
epochsecond=time.time()
print(epochsecond) ##finding second passed since 1970 1st jan

T=time.ctime(1585920389.173065) #finding current time
print(T)
print("/n")

dt=datetime.datetime.today()
print('current Date:{}/{}/{}'.format(dt.day,dt.month,dt.year))
print('current Time:{}/{}/{}'.format(dt.hour,dt.minute,dt.second))
print("/n")

#combining date and time
from datetime import *
d=date(1999,11,15)
t=time(8,30,00)
datetime.combine(d,t)
print(d,t)
print("/n")

#Sorting date
from datetime import *
ldate=[]

d1=date(2020,4,5)
d2=date(2019,4,7)
d3=date(2018,11,23)

ldate.append(d1)
ldate.append(d2)
ldate.append(d3)

ldate.sort()

for d in ldate:
    print(d)
print("/n")

#sleep() method or temporari method to sleep program
from datetime import *
import time
ldate=[]

d1=date(2020,4,5)
d2=date(2019,4,7)
d3=date(2018,11,23)

ldate.append(d1)
ldate.append(d2)
ldate.append(d3)

ldate.sort()

time.sleep(3)

for d in ldate:
    print(d)
print("/n")

#finding the performance of program
from datetime import *
import time

startTime=time.perf_counter()

ldate=[]

d1=date(2020,4,5)
d2=date(2019,4,7)
d3=date(2018,11,23)

ldate.append(d1)
ldate.append(d2)
ldate.append(d3)

ldate.sort()

time.sleep(3)

for d in ldate:
    print(d)

endTime=time.perf_counter()
print("Execution time",endTime-startTime)
