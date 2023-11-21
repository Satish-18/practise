'''
K Nearest Neighbors Project 
    Welcome to the KNN Project! This will be a simple project very similar to the lecture, 
    except you'll be given another data set. 
    Go ahead and just follow the directions below.

'''
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

#KNN_Project_Data csv file into a dataframe 
df = pd.read_csv('KNN_Project_Data')

#Check the head of the dataframe.
print(df.head())

#Use seaborn on the dataframe to create a pairplot with the hue indicated by the TARGET CLASS column.
sns.pairplot(df,hue='TARGET CLASS',palatte='coolwarm')
plt.show()

'''
Standardize the Variables
   
    Time to standardize the variables
'''
    
from sklearn.preprocessing import StandardScaler

#Create a StandardScaler() object called scaler
scaler = StandardScaler()

#Fit scaler to the features.
scaler.fit(df.drop('TARGET CLASS',axis=1))

#Use the .transform() method to transform the features to a scaled version.
scaled_features = scaler.transform(df.drop('TARGET CLASS',axis=1))

#Convert the scaled features to a dataframe and check the head of this dataframe to make sure the scaling worked.
df_feat = pd.DataFrame(scaled_features,columns=df.columns[:-1])
print(df_feat.head(3))


from sklearn.model_selection import train_test_split
#Use train_test_split to split your data into a training set and a testing set.
X = df_feat
y = df['TARGET CLASS']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=101)

#Import KNeighborsClassifier from scikit learn.
from sklearn.neighbors import KNeighborsClassifier

#Create a KNN model instance with n_neighbors=1
knn = KNeighborsClassifier(n_neighbors=1)

#Fit this KNN model to the training data
knn.fit(X_train,y_train)

'''
Predictions and Evaluations
    Let's evaluate our KNN model!
'''

#Use the predict method to predict values using your KNN model and X_test
pred = knn.predict(X_test)

from sklearn.metrics import classification_report,confusion_matrix
#Create a confusion matrix and classification report
print(confusion_matrix(y_test,pred))
print(classification_report(y_test,pred))


'''
Choosing a K Value
    Let's go ahead and use the elbow method to pick a good K Value!
    
     Create a for loop that trains various KNN models with different k values, 
     then keep track of the error_rate for each of these models with a list. 
     
'''
error_rate = []

for i in range(1,40):

	knn = KNeighborsClassifier(n_neighbors=i)
	knn.fit(X_train,y_train)
	pred_i = knn.predict(X_test)
	error_rate.append(np.mean(pred_i != y_test))


plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rate,color='blue',marker='o',markersize=10)
plt.title('Error ratre Vs k value')
plt.xlabel('k')
plt.ylabel('Eror rate')

'''
Retrain with new K Value
    Retrain your model with the best K value (up to you to decide what you want) 
    and re-do the classification report and the confusion matrix
'''
knn = KNeighborsClassifier(n_neighbors=30)
knn.fit(X_train,y_train)
pred = knn.predict(X_test)
print(confusion_matrix(y_test,pred))
print('\n')
print(classification_report(y_test,pred))
