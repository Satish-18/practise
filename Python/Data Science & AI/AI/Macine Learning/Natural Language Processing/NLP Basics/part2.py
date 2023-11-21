import string 
mess = "Sample messege! Notice: it has punctuation"
#print(string.punctuation)

#nopunc = [c for c in mess if c not in string.punctuation]

#print(nopunc)

#Removing the common words from the mess 
from nltk.corpus import stopwords

clean_mess = [words for words in mess.split() if words.lower() not in stopwords.words('english')]
print(clean_mess)