import numpy as np 
import matplotlib.pyplot  as plt  
x = np.arange(0,100)
y = x*2
z = x**2 
print(x,y,z)
'''
1) Create a figure object called fig using plt.figure
2)use axes to ass axis to the figure at [0,0,1,1] cal this new axis as ax
3)Plot (x,y) on this axis and set lables
'''

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_title('title')
plt.show()


###
fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,.5,.2,.2])
ax1.plot(x,y)
ax2.plot(x,y)
plt.show()