import pandas as pd

#Read ecom purches csv files and set the datefrme call ecom
ecom = pd.read_csv('Ecommerce Purchases')
eco.head()

#How many row and columns are there
len(ecom.col)

#What is the average purchases pirce?
ecom['Purchases pirce'].mean()

#How many people have English 'en' as their language of choice on the website
ecom[ecom['language'] == 'en']['language'].count()

#How many people have the job title of Lawyer
ecom[ecom['Job']==['Lawyer']].count()

#How many people made purchases during AM amd PM
ecom['AM or PM'].value_counts()