import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
import seaborn as sns 

#Read built in data from sklearn
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
print(cancer['DESCR'])


df = pd.DataFrame(cancer['data'],columns=cancer['feature_names'])
print(df.head())


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(df)
scaled_data = scaler.transform(df)

#principal component
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(scaled_data)
x_pca = pca.transform(scaled_data)
print(scaled_data.shape)
print(x_pca.shape)

#ploting the transform points
plt.figure(figsize=(8,6))
plt.scatter(x_pca[:,0],x_pca[:,1],c=cancer['target'],cmap='plasma')
plt.xlabel('First component')



print(pca.components_)
plt.ylabel("second component")
plt.show()