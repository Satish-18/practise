'''
Create a function that takes a text file as input and returns the number of words contained
 in the text file. Please take into consideration that some words can be separated by a comma
  with no space. For example "Hi,it's me." would need to be counted as three words

  '''

 def count_words(filepath):
    with open(filepath, 'r') as file:
       text = file.read()
    text = text.replace(",", " ")
    string_list = text.split(" ")
    return len(string_list)
 
print(count_words("words2.txt"))