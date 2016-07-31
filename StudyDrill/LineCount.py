#Descript:This is used for counting the file lines,and print the lines which contain the largest counts of characters
#Version:1.0
#Author:DanyFrank
import os
import sys

filename='test.txt'
max_line=0
max_counts=0
now_line=0

#Read the file,and return
def readfile(filename):
	file_oper=open(filename,'r')
	return file_oper

#read the file and save the line-characters to the dictionary
def read(filename):
	global now_line    
	file_oper=readfile(filename)
	while True:
		text=file_oper.readline()
		readCounts(text)
		now_line+=1
		if not text:
			break
	readCounts(text)
	file_oper.close()

def readCounts(text):
	global max_line,max_counts,now_line
	text_arr=[]
	text_arr=text.split(' ')
	words_counts=len(text_arr)
	print "Line %d, Words:%d" % (now_line,words_counts)
	if max_counts<words_counts:
		max_counts=words_counts
		max_line=now_line

read(filename)
print "Result: Line %d ,Words %d" % (max_line,max_counts)
