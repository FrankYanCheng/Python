#Homework
from sys import argv
from sys import exit
script,name=argv
def Paradise():
    print "Welcome to Paradise~~~~"
    par_list=['Angle','Cupid','God']
    counts=0
    for role in par_list:
        print "%d %s" % (counts,role)
        counts+=1
    try: 
        style=input("You want to be a ?Input the number!")
        out(par_list[style])        
    except:
        out("Wrong")
        exit(0)
def Human_World():
    out("are born in the small city long long ago")
    print "God write career,input 'end' to end the work"
    car_list=[]
    while True:
        career=raw_input()
        if career=="end":
            break
        car_list.append(career)
    out("hi~Could you tell me which person you want to be?")
    counts=0
    for role in car_list:
        print "%d %s" % (counts,role)
        counts+=1
    input_role=raw_input("Please input the role\n")
    if input_role in car_list:
        out(input_role)
    else:
        out("You may want to Paradise~~~")
        Paradise() 
    
def out(output):
    global name
    print "%s : %s" % (name,output)
print name
Human_World()
