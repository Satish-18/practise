import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer

#sklearn built in datasets
cancer = load_breast_cancer()
#print(cancer.keys())

data_feat = pd.DataFrame(cancer['data'],columns=cancer['feature_names'])
#print(data_feat)



from sklearn.model_selection import train_test_split
x = data_feat
y = cancer['target']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=101)


from sklearn.svm import SVC
model = SVC()
model.fit(x_train,y_train)
pred = model.predict(x_test)


from sklearn.metrics import classification_report,confusion_matrics
print(classification_report(y_test,predictions))
print(confusion_matrics(y_test,predictions))

from sklearn.grid_search import  GridSearchCV
param_grid = {'c':[0.1,1,11,100,1000],'gamma':[1,0.1,0.01,0.001,0.0001]}
grid = GridSearchCV(SVC(),param_grid,verbose=3)
grid.fit(x_train,y_train)
grid_prediction = grid.predict(x_test)
print(classification_report(y_test,predictions))
print(confusion_matrics(y_test,predictions))
