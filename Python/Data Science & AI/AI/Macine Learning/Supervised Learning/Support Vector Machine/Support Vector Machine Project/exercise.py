'''
Support Vector Machines Project
    "Welcome to your Support Vector Machine Project! Just follow along with the notebook and instructions below.
    We will be analyzing the famous iris data set!
    The Data
    "For this series of lectures, we will be using the famous [Iris flower data set](http://en.wikipedia.org/wiki/Iris_flower_data_set).
    "The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by Sir Ronald Fisher in the 1936 as an example of discriminant analysis.

'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Use seaborn to get the iris data
iris = sns.load_dataset('iris')

#The Iris Virginica

#Create a pairplot of the data set. Which flower species seems to be the most separable?
sns.pairplot(iris,hue='species')
#plt.show()



from sklearn.model_selection import train_test_split

#Split your data into a training set and a testing set.
x = iris.drop('species',axis=1)
y = iris['species']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=101)

#Now its time to train a Support Vector Machine Classifier.
#Call the SVC() model from sklearn and fit the model to the training data.
from sklearn.svm import SVC
model = SVC()
model.fit(x_train,y_train)
predictions = model.predict(x_test)


from sklearn.metrics import classification_report
#Now get predictions from the model and create a confusion matrix and a classification report.
#print(classification_report(y_test,predictions))


#Grid search
from sklearn.model_selection import  GridSearchCV
#Create a dictionary called param_grid and fill out some parameters for C and gamma.
param_grid = {'c':[0.1,1,11,100],'gamma':[1,0.1,0.01,0.001]}

grid = GridSearchCV(SVC(),param_grid,verbose=3)
grid.fit(x_train,y_train)

#Now take that grid model and create some predictions using the test
grid_prediction = grid.predict(x_test)
print(classification_report(y_test,predictions))

