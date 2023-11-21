import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 

#Read in the College_Data file using read_csv. Figure out how to set the first column as the index.
data = pd.read_csv('College_Data')

#Check the head of the data
print(data.head())


#It's time to create some data visualizations!
#Create a scatterplot of Grad.Rate versus Room.Board where the points are colored by the Private column

sns.lmplot(x='Room.Board',y='Grad.Rate',data=data,hue='Private',fit_reg=False)
#Create a stacked histogram showing Out of State Tuition based on the Private column. Try doing this using [sns.FacetGrid](https://stanford.edu/~mwaskom/software/seaborn/generated/seaborn.FacetGrid.html). If that is too tricky, see if you can do it just by using two instances of pandas.plot(kind='hist')
g = sns.FacetGrid(data,hue='Private',palette='coolwarm',size=6,aspect=2)
g = g.map(plt.hist,'Outstate',bins=20,alpha=0.7)
plt.show()

#K Means Cluster Creation
#Import KMeans from SciKit Learn
from sklearn.cluster import KMeans

#Create an instance of a K Means model with 2 clusters.
kmeas = KMeans(n_clusters=4)

#Fit the model to all the data except for the Private label.
kmeas.fit(data.drop('Private',axis=1))

# What are the cluster center vectors?
print(KMeans.cluster_centers_)