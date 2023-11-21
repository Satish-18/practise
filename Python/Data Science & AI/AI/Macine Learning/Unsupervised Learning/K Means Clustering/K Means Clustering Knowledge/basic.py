import seaborn as sns
import matplotlib.pyplot as plt 



from sklearn.datasets import make_blobs
data = make_blobs(n_samples=200,n_features=2,centers=4,cluster_std=1.8,random_state=101)
#print(data)


#use k means algorithm
from sklearn.cluster import KMeans
kmeas = KMeans(n_clusters=4)
kmeas.fit(data[0])
