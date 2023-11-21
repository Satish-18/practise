#\d=0 to 9 \D=does opposite to \d \s \S /w \W \b \A \Z
## searching the string
import re
st="Hi this  is satish subedi"
result=re.search(r'o\w\w',st)
print(result)

##findall method
st="Hi this  is satish subedi"
result=re.findall(r'o\w\w',st)
print(result)

#match method
st="Hi this  is satish subedi"
result=re.match(r'T\w\w',st)
print(result)

#split method
st="Hi 1 this 23  is satish 45 subedi"
result=re.split(r'\d+',st)
print(result)

#substitute method
#replace string with new
st="Hi this  is satish subedi"
result=re.sub(r'is','not',st)
print(result)

#reurning matching dates
st="Hi 1 this  1-3-2020  23 satish 12-12-2010 subedi"
result=re.findall(r'\d{1,2}-\d{4}',st)
print(result)


#Using special chatacters
st="Hi this  is satish subedi"
result=re.findall(r'^T\ww*',st)
print(result)
