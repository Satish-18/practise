import nltk

#nltk.downlode_shell()->For downloding nltk packages
#UCi.com ->For datasets



#Reading the messeges of the file
messeges = [line.rstrip() for line in open('SMSSpanCollection')]
print(len(messeges))


#Printing first 10 messeges using enumerate
for mess_no,messeges in enumerate(messeges[:10]):
	print(mess_no,messeges)
	print('\n')


'''
import pandas as pd 
import numpy as np
df = pd.read_csv('readme')
#print(df.head())
#df.describe()
#df.gropupby('label')describe()bbb
'''