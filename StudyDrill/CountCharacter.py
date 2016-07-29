#This is a train for counting character for a web,import to a web
import urllib2
import urllib
import pprint
import web
import operator
text=open('test.txt','r')
info=text.read()
text.close()

dic={}

for char in info.upper():
    dic.setdefault(char,0)
    dic[char]=dic[char]+1

#dic=sorted(dic.iteritems(),key=lambda d:d[1],reverse=True)
#print pprint.pformate(dic)

diclength=len(info)
diclength=float(diclength)
for key,value in dic.items():  
    value=value/diclength*100
    print key,
    print 'ratio {:04.2f}'.format(value)

