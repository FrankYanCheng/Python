#Python Training
from bs4 import BeautifulSoup
import urllib
import urllib2
import re
url="https://movie.douban.com"
request=urllib2.Request(url)
response=urllib2.urlopen(request)
content=response.read()
soup=BeautifulSoup(content,"lxml")
#print soup.img.attrs
#print soup.head.contents[0]
#for child in soup.body.children:
    #print child
for img in soup.find_all("img"):
        if img.has_key("alt"):
            print img["alt"]
            print img["src"]
        
