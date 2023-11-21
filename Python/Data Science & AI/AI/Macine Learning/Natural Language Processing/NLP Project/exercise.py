import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

#Read the yelp.csv file and set it as a dataframe called yelp.
yelp = pd.read_csv('yelp.csv')

#Create a new column called \"text length\" which is the number of words in the text column
yelp['text length'] = yelp['text'].apply(len)

'''
#Check the head, info , and describe methods on yelp
print(yelp.head())
print(yelp.info())
print(yelp.describe())


#Use FacetGrid from the seaborn library to create a grid of 5 histograms of text length based off 
#of the star ratings. Reference the seaborn documentation for hints on this
g = sns.FacetGrid(yelp,col='stars')
g.map(plt.hist,'text length',bins=50)
plt.show()

#Use groupby to get the mean values of the numerical columns, you should be able to create this dataframe with the operation
stars = yelp.groupby('stars').mean()
print(stars)
'''

#Create a dataframe called yelp_class that contains the columns of yelp dataframe but for only the 1 or 5 star reviews.
yelp_class = yelp[(yelp['stars']==1) | (yelp['stars']==5)]
#print(yelp_class.info())

#Create two objects X and y. X will be the 'text' column of yelp_class and y will be the 'stars' column of yelp_class. (Your features and target/labels)
X = yelp_class['text']
y = yelp_class['stars']

#Import CountVectorizer and create a CountVectorizer objec
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()

#Use the fit_transform method on the CountVectorizer object and pass in X (the 'text' column). Save this result by overwriting X
X = cv.fit_transform(X)

#Let's split our data into training and testing data.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3,random_state=101)

#Import MultinomialNB and create an instance of the estimator and call is nb
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()

#Now fit nb using the training data.
nb.fit(X_train,y_train)

#Predictions and Evaluations
#Time to see how our model did!
#Use the predict method off of nb to predict labels from X_test
predictions = nb.predict(X_test)

#Create a confusion matrix and classification report using these predictions and y_test
from sklearn.metrics import confusion_matrix,classification_report
print(confusion_matrix(y_test,predictions))
print('\\n')
print(classification_report(y_test,predictions))