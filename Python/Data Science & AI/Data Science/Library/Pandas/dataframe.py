import numpy as np 
import pandas as pd 

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4),['a','b','c','d','e'],['w','x','y','z'])

print(df)

#Now grabing the certain items

print(df['w'])

#selecting the number of column
print(df[['w','z']])

#Conditional dataframe

print(df[df>0])#it gives the null to unsatisfied condition

print(df[df['w']>0]) #Gives only satidfied values


#multiple conditioning(can only use & |)
print(df[(df['w']>0) & (df['y']>1)])

#Level index
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
print(df)

print(df.loc['G2'].loc[2]['B'])


#Data input and output
'''
CSV EXCEL HTML SQL

'''
#reading CSV FILE
df = pd.read_csv('example.csv')
print(df)

#Reading and writing excel files
pd.read_excel('excel_sample.xlsx',sheetname='Sheet1')

#Reading the html files(webscraping)
data = pd.read_html('https://google.com/ndj.html')

#Reading the SQL files
from sqlalchemy import create_engine
engine = create_engine('sqlite://:memory:')
df.to_sql('my_table',engine)
sqldf = pd.read_sql('my_table',con=engine)