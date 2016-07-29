from bs4 import BeautifulSoup
import urllib2
import urllib
request=urllib2.Request("http://www.baidu.com")
response=urllib2.urlopen(request)
html=response.read()
soup=BeautifulSoup(html)
#print type(soup.head)
print soup.p.string
