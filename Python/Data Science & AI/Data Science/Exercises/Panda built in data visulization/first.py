import numpy as np 
import pandas as pd 
import seaborn as sns

#df1 = pd.read_csv('df1',index_col=0)
#print(df1.head(2))

df2 = pd.read_csv('df2',index_col=0)
print(df2.head())

print(df2.plot.area())
