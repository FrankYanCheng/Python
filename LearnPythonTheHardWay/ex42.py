class Animal(object):
    def __init__(self):
        print "Animal"
    def hello(self):
        print "Hello Animal"

class Dog(Animal):
    #def __init__(self):
        #print "Dog"
    def hello(self):
        print "Hello Dog"
a=Animal()
a.hello()
b=Dog()
b.hello()
