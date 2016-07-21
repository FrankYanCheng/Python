from bs4 import BeautifulSoup
html="""
<a class='Hello World class'>This is a test</a>
"""
soup=BeautifulSoup(html,"lxml")
#print soup.a.string
print soup.name
