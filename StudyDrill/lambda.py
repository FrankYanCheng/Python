#test1
f=lambda x,y,z:x+y+x
print f(1,2,3)

#test2
n=5
print reduce(lambda x,y:x*y,range(1,n+1))

#test3
def action(x):
	return lambda y:x+y
a=action(2)
print a(22)

#test4
b=lambda x:lambda y:x+y
a=b(3)
print a(2)
print (b(2))(2)
