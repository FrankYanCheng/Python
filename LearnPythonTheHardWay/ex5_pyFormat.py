#Basic formatting

#print '%s %s'% ('one','two')
#print '{} {}'.format('one','two')

#Value conversion
#class Data(object):
#    def __str__(self):
#        return 'str'
#    def __repr__(self):
#        return 'repr'
#print '%s %r' %(Data(),Data())
#print '{0!s} {0!r}'.format(Data())

#Padding and aligning strings
#Align right
#print '%10s' % ('test',)
#print '{:>10}'.format('test')
#Align left
#print '%-10s' % ('test',)
#print '{:10}'.format('test')
#print '%*s' % ((-8),'test')
#print '{:<{}}'.format('test',8)
#print '{:_<10}'.format('test')
#print '{:^30}'.format('test')

#Truncating long strings
#print '%.5s' % ('xylophone',)
#print '{:.5}'.format('xylophone')
#print '%.*s' % (7,'xylophone')
#print '{:.{}}'.format('xylophone',7)

#Combining truncating and padding
#print '%-10.5s' % ('xylophone',)
#print '{:_<10.5}'.format('xylophone')

#Numbers
#print '%d' % (42,)
#print '{:d}'.format(42)
#print '%f' % (3.141592653589793)
#print '{:f}'.format(3.141592653589793)

#Padding numbers
#print '%4d' % (42,)
#print '{:4d}'.format(42)
#print '%06.2f' % (3.141592653589793,)
#print '{:06.2f}'.format(3.141592653589793)
#print '%0.4d' % (42,)
#print '{:04d}'.format(42)

#Signed numbers
#print '%+d' % (42,)
#print '{:+d}'.format(42)
#print '% d' % ((- 23),)
#print '{: d}'.format((- 23))
#print '% d' % (42,)
#print '{:d}'.format(42)
#print '{:=5d}'.format((-23))

#Named placeholders
#data={'first':'Hodor','last':'Hodor!'}
#print '%(first)s %(last)s' % data
#print '{first} {last}'.format(**data)
#print '{first} {last}'.format(first='Hodor',last='Hodor!')

#Getitem and Getattr
#person={'first':'Jean-Luc','last':'Picard'}
#print '{p[first]} {p[last]}'.format(p=person)

#class Plant(object):
    #type='tree'
#print '{p.type}'.format(p=Plant())
#class Plant(object):
    #type='tree'
    #kinds=[{'name':'oak'},{'name':'maple'}]
#print '{p.type}:{p.kinds[0][name]}'.format(p=Plant())

#DateTime
#from datetime import datetime
#print '{:%Y-%m-%d %H:%M}'.format(datetime(2001,2,3,4,5))

#Custom objects
class HAL9000(object):
    def __format__(self,format):
        if(format=='Hello'):
            return 'World'
        return 'HAL 9000'
print '{:Hello}'.format(HAL9000())
print '{:test}'.format(HAL9000())
