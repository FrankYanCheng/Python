import urllib2
import urllib
import re
def write_img(filename,imgurl):
    img=urllib.urlopen(imgurl)
    data=img.read()
    w=open(filename,'wb')
    w.write(data)
    w.close()

def crawler(page,total):
    url="http://www.ugirls.com/Index/Search/Magazine-"+str(total)+"-"+str(page)+".html"
    headers={
         "User-Agent":"Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
    }   
    counts=0
    request=urllib2.Request(url,headers=headers) 
    response=urllib2.urlopen(request)
    content=response.read()
    pattern=re.compile('data-original="(.*?)".*?>')
    items=re.findall(pattern,content)
    for item in items:
        filename=str(total)+"-"+str(page)+"-"+str(counts)+'.jpg'
        print filename
        write_img(filename,item)
        counts=counts+1

def start(page,total):
    while total<60:
        if page>5:
            total=total+1
            page=1
        else:
            try:
                crawler(page,total)
            except:
                print "wait......"
        page=page+1
start(1,30)
    
