import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


#Get the data
columns_names = ['user_id','item_id','rating','timestamp']
df = pd.read_csv('u.data',sep='\t',names=columns_names)
#print(df.head())


movies_title = pd.read_csv('Movie_Id_Titles')
#print(movies_title.head())

#making connection between item_id and title of movies
df = pd.merge(df,movies_title,on='item_id')
#print(df)


#finding movies with the 5 beat ratings
srt = df.groupby('title')['rating'].mean().sort_values(ascending=False).head(5)

#Which movies have most ratings
mrt = df.groupby('title')['rating'].count().sort_values(ascending=False).head()
print(mrt)