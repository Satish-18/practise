import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.model_selection import train_test_split


df = pd.read_csv('USA_Housing.csv')
#print(df.info())

sns.pairplot(df)
plt.show()

#Try to predict the price of the house

sns.distplot(df['Price'])
plt.show()

sns.heatmap(df.corr(),annot=True)
plt.show()

#Scikit learn model
x = np.arange(1,11).reshape(-1,1)
y = np.arange(1,11).reshape(-1,1)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.4,random_state=101)

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(x_train,y_train)
#print(lm.intercept_)


#Prediction using aklearn
Prediction = lm.predict(x_test)
print(Prediction)

#plt.scatter(y_test,Prediction)
#sns.distplot(y_test-Prediction)
#plt.show()

#checking the metrices error
from sklearn import metrics
print(metrics.mean_absolute_error(y_test,Prediction))
print(metrics.mean_squared_error(y_test,Prediction))

print(np.sqrt(metrics.mean_squared_error(y_test,Prediction)))