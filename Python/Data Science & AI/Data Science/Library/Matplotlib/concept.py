import matplotlib.pyplot as plt 


import numpy as np

x = np.linspace(0,5,11)

y = x**2

print(x)
print(y)
plt.subplot(1,2,1)
plt.plot(x,y,'r')

plt.subplot(1,2,2)
plt.plot(y,x,'b')

plt.show()

#Object oriented method
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
plt.show()

fig,axes = plt.subplots(nrows=1,ncols=2)
for current_ax in axes:
	current_ax.plot(x,y)
plt.show()

#Figure size and DPI
fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(8,2))
axes[0].plot(x,y)
axes[1].plot(y,x)
plt.tight_layout()
plt.show()


#Plot Apperance
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,color='purple',linewidth=3,alpha=0.5,linestyle='-')
plt.show()