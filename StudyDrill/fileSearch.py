#This is used for finding files
import os
root='/'
dirlist=[]
file_open=''
def write(text,file_open):
	file_open.write(text)
	
def dirfile(dirname,files,file_open):
	sperateName='dir'
	sperate='-------%s----------' % (sperateName)
	write(sperate,file_open)
	write(dirname,file_open)
 	sperateName='file'
	write(sperate,file_open)
	for filename in files:
		write(filename,file_open)


def listdir(root):
	global file_open
	filesName=[]
	dirName=root
	stack=os.listdir(dirName)
	while stack:
		temp=stack.pop()
		print temp
		if os.path.isfile(temp):
			print os.path.abspath(temp)
		elif os.path.isdir(temp):
			tempList=os.listdir(temp)
			stack.push(tempList)
		else:
			print stack.pop()

listdir(root)
test=os.system('du -h')
print test

