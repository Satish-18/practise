'''
SF SALARIES EXERSCISE
'''
import pandas as pd 

sal = pd.read_csv('salaries.csv')
print(sal.head(2))

#use info method to find out how many enteries are there
print(sal.info())


#What is the average basepay
print(sal['Basepay'].mean())

#What is the highest amount of overtimepayh in the datasate
print(sal['Overtimepay'].max())

#What is the job title of FOSEPH DRIDCOLL
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])

#How much does JOSEPH DRISCOLL makes including benifits
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])


#What is he name of highest paid person
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName'])

or
print(sal.loc[sal['TotalPayBenefits'].idxmax()])

#What is the lowest paid person did you notice domething strange about that person 
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]['EmployeeName'])
 or 

print(sla.iloc[sal['TotalPayBenefits'].argmin()])

#What is the average base pay of all employee per year
print(sal.groupby('year').mean()['Basepay'])

#How many unique job are there
print(sal['JobTitle'].unique())

#What are the top 5 common jobs
print(sal['JobTitle'].value_counts().head(5))

#How may job title were repreasented by only ome person in 2013
print(sum(sal[sal['Year']==2013]['JobTitle'].value_counts()==1)

#Hoew many people have word chief in their name
def chief_str(title):
	if 'chief' in title.lower().split():
		return True
	else:
		return False

sum(sal['JobTitle'].applay(lambda x:chief_str(x)))


#Is there a correlation between length of the job title string and salary
sal['title_len'] = sal['JobTitle'].apply(len)
sal[['TotalPayBenefits','title_len']].corr()