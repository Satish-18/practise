'''
Congratulations! You just got some contract work with an Ecommerce company based in New York City that sells clothing online but they also have in-store style and clothing advice sessions.
 Customers come in to the store, have sessions/meetings with a personal stylist, then they can go home and order either on a mobile app or website for the clothes they want.
    
    The company is trying to decide whether to focus their efforts on their mobile app experience or their website. They've hired you on contract to help them figure it out! Let's get 
    started!
    
    "Just follow the steps below to analyze the customer data (it's fake, don't worry I didn't give you real credit card numbers or emails)."
  '''

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns



#Read in the Ecommerce Customers csv file as a DataFrame called customers.
customers = pd.read_csv("Ecommerce Customers")
print(customers)

#Check the head of customers, and check out its info() and describe() methods.
print(customers.head())

print(customers.info())

print(customers.describe())

#Use seaborn to create a jointplot to compare the Time on Website and Yearly Amount Spent columns. Does the correlation make sense?

sns.jointplot(data=customers,x='Time on Website ',y='Yearly Amount Spent')
plt.show()

#Use jointplot to create a 2D hex bin plot comparing Time on App and Length of Membership.
sns.jointplot(data=customers,x='Time on App',y='Length of Membership',kind='hex')
plt.show()

#Let's explore these types of relationships across the entire data set.
#Use [pairplot](https://stanford.edu/~mwaskom/software/seaborn/tutorial/axis_grids.html#plotting-pairwise-relationships-with-pairgrid-and-pairplot) to recreate the plot below.
#(Don't worry about the the colors)
sns.pairplot(customers)
plt.show()

#Based off this plot what looks to be the most correlated feature with Yearly Amount Spent?
ans: Length of Membership

#Create a linear model plot (using seaborn's lmplot) of  Yearly Amount Spent vs. Length of Membership. 
sns.lmplot(x='Length of Membership',y='Yearly Amount Spent',data=customers)
plt.show()

'''
Training and Testing Data
  
Now that we've explored the data a bit, let's go ahead and split the data into training and testing sets.
Set a variable X equal to the numerical features of the customers and a variable y equal to the Yearly Amount Spent column.
'''

print(customers.columns)
y = customers['Yearly Amount Spent']
x = customers[[ 'Avg. Session Length', 'Time on App','Time on Website', 'Length of Membership', 'Yearly Amount Spent']]

#Use model_selection.train_test_split from sklearn to split the data into training and testing sets. Set test_size=0.3 and random_state=101
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=101)


# Training the Model
#Now its time to train our model on our training data!   
#Import LinearRegression from sklearn.linear_model

from sklearn.linear_model import LinearRegression

#Create an instance of a LinearRegression() model named lm
lm = LinearRegression()

#Train/fit lm on the training data.
lm.fit(x_train,y_train)

#Print out the coefficients of the model
print(lm.coef_)


predictions = lm.predict(x_test)

'''
Predicting Test Data
Now that we have fit our model, let's evaluate its performance by predicting off the test values!
Use lm.predict() to predict off the X_test set of the data.
'''

#Create a scatterplot of the real test values versus the predicted values.
plt.scatter(y_test,predictions)
plt.xlabel('Y test(True values)')
plt.ylabel('Predicted values')
plt.show()


'''
Evaluating the Model
Let's evaluate our model performance by calculating the residual sum of squares and the explained variance score (R^2).
Calculate the Mean Absolute Error, Mean Squared Error, and the Root Mean Squared Error. Refer to the lecture or to Wikipedia for the formulas
  
'''
from sklearn import metrics
print(metrics.mean_absolute_error(y_test,predictions))
print(metrics.mean_squared_error(y_test,predictions))
print(np.sqrt(metrics.mean_squared_error(y_test,predictions)))

'''
Residuals
You should have gotten a very good model with a good fit. Let's quickly explore the residuals to make sure everything was okay with our data. 
Plot a histogram of the residuals and make sure it looks normally distributed. Use either seaborn distplot, or just plt.hist().
'''

sns.distplot((y_test-predictions),bins=50)
plt.show()

#Recreate the dataframe below.
cdf = pd.DataFrame(lm.coef_,x.columns,columns=['coeff'])
print(cdf)