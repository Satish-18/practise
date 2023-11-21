
import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
iris = sns.load_dataset('iris')
tips.head()



#Distribution Plot
sns.distplot(tips['total_bill'],kde=False,bins=100)
plt.show()

sns.jointplot(x='total_bill',y='tip',data=tips)
sns.pairplot(tips,hue='sex')
plt.show()


#Categorical plots
sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)
plt.show()

#matrix plot
tc = tips.corr()
#Heat map visualization
sns.heatmap(tc)
plt.show()

fp = flights.pivot_table(index='month',columns='year',values='passengers')
sns.heatmap(fp)
plt.show()

sns.clustermap(fp)


#GRIDS
g = sns.PairGrid(iris)
g.map_diag(sns.distplot)
#g.map_upper(sns.scatter)
g.map_lower(sns.kdeplot)
plt.show()

#Regerssion plot
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex')
plt.show()