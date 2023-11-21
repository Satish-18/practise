
#Downloding the html file using an url
import urllib.request
try:
    url=urllib.request.urlopen("https://www.python.org/")
    content=url.read()
    url.close()
except urlliberror.HTTPError:
    print("The web page is not found")
    exit()

f=open("python.html","wb")
f.write(content)


#Downloding a image from internet
import urllib.request
url="https://www.python.org/static/img/python-logo.png"
urllib.request.urlretrieve(url,"python.png")
