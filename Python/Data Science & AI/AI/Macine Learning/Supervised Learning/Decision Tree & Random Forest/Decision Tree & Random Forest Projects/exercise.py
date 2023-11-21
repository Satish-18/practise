import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

'''
Random Forest Project 
    
    "For this project we will be exploring publicly available data from [LendingClub.com](www.lendingclub.com). 
    Lending Club connects people who need money (borrowers) with people who have money (investors). Hopefully, as an investor you 
    would want to invest in people who showed a profile of having a high 
    probability of paying you back. We will try to create a model that will help predict this.
    "Lending club had a [very interesting year in 2016](https://en.wikipedia.org/wiki/Lending_Club#2016), so let's 
    check out some of their data and keep the context in mind. This data is from before they even went public.
    "We will use lending data from 2007-2010 and be trying to classify and predict whether or not the borrower paid back their loan in full. 
    "Here are what the columns represent:
    credit.policy: 1 if the customer meets the credit underwriting criteria of LendingClub.com, and 0 otherwise
    purpose: The purpose of the loan (takes values  credit_card debt_consolidation educational major_purchase
    , small_business, and all_other).
    int.rate: The interest rate of the loan, as a proportion (a rate of 11% would be stored as 0.11). Borrowers judged by LendingClub.com
     to be more risky are assigned higher interest rates.
    installment: The monthly installments owed by the borrower if the loan is funded.
    log.annual.inc: The natural log of the self-reported annual income of the borrower.
    dti: The debt-to-income ratio of the borrower (amount of debt divided by annual income).
    fico: The FICO credit score of the borrower.
    days.with.cr.line: The number of days the borrower has had a credit line.
    revol.bal: The borrower's revolving balance (amount unpaid at the end of the credit card billing cycle).
    revol.util: The borrower's revolving line utilization rate (the amount of the credit line used relative to total credit available).
    inq.last.6mths: The borrower's number of inquiries by creditors in the last 6 months.
    delinq.2yrs: The number of times the borrower had been 30+ days past due on a payment in the past 2 years.
    pub
'''
#read the data
df = pd.read_csv('loan_data.csv')
'''
#Check out the info(), head(), and describe() methods on loans.
print(df.head())
print(df.info())
print(df.describe())
'''

'''
# Exploratory Data Analysis
    "Let's do some data visualization! We'll use seaborn and pandas built-in plotting capabilities, but feel free to use whatever library you want. 
    Don't worry about the colors matching, just worry about getting the main idea of the plot.
    Create a histogram of two FICO distributions on top of each other, one for each credit.policy outcome.
'''
'''
plt.figure(figsize=(10,6))
df[df['credit.policy']==1]['fico'].hist(bins=40,label='credit polecy=1')
df[df['credit.policy']==0]['fico'].hist(bins=40,label='credit polecy=0')
plt.legend()
plt.show()

#Create a similar figure, except this time select by the not.fully.paid column.
plt.figure(figsize=(10,6))
df[df['not.fully.paid']==1]['fico'].hist(bins=40,label='not.fully.paid=1')
df[df['not.fully.paid']==0]['fico'].hist(bins=40,label='not.fully.paid=0')
plt.legend()
plt.show()
#Create a countplot using seaborn showing the counts of loans by purpose,
#with the color hue defined by not.fully.paid.
plt.figure(figsize=(10,7))
sns.countplot(x='purpose',hue='not.fully.paid',data=df)
plt.show()

#Let's see the trend between FICO score and interest rate. Recreate the following joint plot 
sns.jointplot(x='fico',y='int.rate',data=df)
plt.show()

#Create the following lmplots to see if the trend differed between not.fully.paid and credit.policy. Check the documentation for lmplot()
#if you can't figure out how to separate it into columns.
plt.figure(figsize=(10,6))
sns.lmplot(y='int.rate',x='fico',data=df,hue='credit.policy',col='not.fully.paid')
plt.show()
'''
'''
Let's get ready to set up our data for our Random Forest Classification Model!
" Categorical Features
  
    "Notice that the **purpose** column as categorical
    "That means we need to transform them using dummy variables so sklearn will be able to understand them. Let's do this in one clean step using pd.get_dummies.
    "Let's show you a way of dealing with these columns that can be expanded to multiple categorical features if necessary.
   
'''
#Create a list of 1 element containing the string 'purpose'. Call this list cat_feats.
cat_feats = ['purpose']

#Now use pd.get_dummies(loans,columns=cat_feats,drop_first=True) to create a fixed larger dataframe that has new 
#feature columns with dummy variables.Set this dataframe as final_data.
final_data = pd.get_dummies(df,columns=cat_feats,drop_first=True)
#print(final_data.info())

from sklearn.model_selection import train_test_split
#Use sklearn to split your data into a training set and a testing set
x = final_data.drop('not.fully.paid',axis=1)
y = final_data['not.fully.paid']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=101)

#Training a Decision Tree Model
#Let's start by training a single decision tree first!
from sklearn.tree import DecisionTreeClassifier

#Create an instance of DecisionTreeClassifier()
dtc = DecisionTreeClassifier()

#Predictions and Evaluation of Decision Tree
dtc.fit(x_train,y_train)
pred = dtc.predict(x_test)

#Create predictions from the test set and create a classification report and a confusion matrix.
from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(y_test,pred))
print(classification_report(y_test,pred))


'''
Training the Random Forest model
    Now its time to train our model!
    
    Create an instance of the RandomForestClassifier class and fit it to our training data from the previous step.
   
'''
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=300)
#Predictions and Evaluation
rfc.fit(x_train,y_train)
preds = rfc.predict(x_test)
print(confusion_matrix(y_test,preds))
print(classification_report(y_test,preds))