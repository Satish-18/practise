
#Write code  in order to match the word Bitcoin at the beginning of the string using the match() method.


import re
 
s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."
 
result = re.match("Bitcoin", s)
 
print(result.group())