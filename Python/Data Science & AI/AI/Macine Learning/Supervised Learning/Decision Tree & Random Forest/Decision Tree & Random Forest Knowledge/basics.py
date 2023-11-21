import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

#read the data
df = pd.read_csv('Kyphosis.csv')
#print(df.head())

#sns.pairplot(df,hue='Kyphosis')
#plt.show()

from sklearn.model_selection import train_test_split

x = df.drop('Kyphosis',axis=1)
y = df['Kyphosis']
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)

from sklearn.tree import DecisionTreeClassifier
dtree = DecisionTreeClassifier()
dtree.fit(x_train,y_train)

pred = dtree.predict(x_test)

from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(y_test,pred))
print(classification_report(y_test,pred))

#Random forest model
from sklearn.ensemble import RandomForestClassifier
rforest = RandomForestClassifier(n_estimators=200)
rforest.fit(x_train,y_train)
rforest_pred = rforest.predict(x_test)
print(confusion_matrix(y_test,rforest_pred))
print(classification_report(y_test,rforest_pred))
