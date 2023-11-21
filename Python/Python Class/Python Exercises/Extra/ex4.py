#Create a script that let the user type in a search term and then the program opens the browser and searches the term on Google.

 
'''
import webbrowser
 
query = input("Input your query: ")
webbrowser.open("https://google.com/search?q=%s" % query)
'''

'''
Please plot the data of this file into a graph of x and y axis.

Answer 1: 

import pandas
import pylab as plt
 
data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data.plot(x='x', y='y', kind='scatter')
plt.show()


Please concatenate this file with this one to a single text file. The content of the output file should look like in the expected output.

Answer 1: 

import pandas
 
data1 = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data2 = pandas.read_csv("sampledata_x_2.txt")
data12 = pandas.concat([data1, data2])
data12.to_csv("sampledata12.txt", index=None)

Create a script that reads this file, multiplies its values by two and saves the output in a new text file.

Answer: 

import pandas
 
data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data_2 = data * 2
data_2.to_csv("sampledata_x_2.txt", index=None)
'''