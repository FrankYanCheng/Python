#Descript:This is used for counting the file line,and print the line which contain the largest characters
#Version:1.0
#Author:DanyFrank
import os
import sys

filename='test.txt'
#Read the file,and return
def readfile(filename):
    file_oper=open(filename,'r')
    return file_oper
def test():
    global filename    
    file_oper=readfile(filename)
    print file_oper.read()
    file_oper.close()
test()
