'''
This is my version,I want to see how many lines of codes I need~~~
'''
import re
import uuid

dicIdWord={}
#Read the words from the text
def words_sperate(text):
	return re.findall('[a-z]+',text.lower())

#Read the filename
def read_text(filename):
	fileOpen=open(filename,'r')
	text=fileOpen.read()
	fileOpen.close()
	return words_sperate(text)

#Return the total numbers of words
def words_counts():	
	words=read_text('cut_test.txt')
	return len(words)

#Words dictionary initation
def words_dic_init(dic,words):
	for index in range(0,len(words)):
		word=words[index]
		dic.setdefault(word,1)
		dic[word]+=1

#Words dictionary Add for edition_number
#return dictionay(word,dictionary(originValue,number))
def words_dic_add(dic,word,originWord):
	global dicIdWord
	dicIdWord.setdefault(word,0)
	
		
		
		
		
	
#Return the edits1 dictionary
def words_edits1(dic):
	editsDic={}
	tempWord=''
	alphabet='qwertyuioplkjhgfdsazxcvbnm'
	alphabetLen=len(alphabet)
	counts=0.0
	ration=0
	dicLen=len(dic)
	print dicLen
	for word in dic:
		wordLen=len(word)
		counts+=1
		ration=counts/dicLen
		print "%03.2f %s \r" % (ration*100,'%'),
		
		#Splits and deletes,Insert
		for wordIndex in range(0,wordLen):
			#insert
			for insertPosition in range(0,alphabetLen):
                        	insertWord=word[0:wordIndex]+alphabet[insertPosition]+word[wordIndex:len(word)]  
				words_dic_add(editsDic,insertWord,word)
			#split
			splitWord=(word[:wordIndex],word[wordIndex:])
			words_dic_add(editsDic,splitWord,word)
			#delete
			deleteWord=word[0:wordIndex]+word[wordIndex+1:len(word)]
			words_dic_add(editsDic,deleteWord,word)
			#replaces
                	for alphaIndex in range(0,alphabetLen):
                        	deleteWord=word[0:wordIndex]+alphabet[alphaIndex]+word[wordIndex+1:len(word)]
				words_dic_add(editsDic,deleteWord,word)
        

		#transports
		for wordIndex in range(0,wordLen-1):	
			transWord=""
			listWord=list(word)
			temp=listWord[wordIndex]
			listWord[wordIndex]=listWord[wordIndex+1]
			listWord[wordIndex+1]=temp
			transWord=tempWord.join(listWord)
			words_dic_add(editsDic,transWord,word)
		
	return editsDic

def init(filename):
	words=read_text(filename)	
	dic={}
	words_dic_init(dic,words)
	editsDicFirst=words_edits1(dic)
	#editsDicSecond=words_edits1(editsDicFirst)
	word=raw_input('Please input  alphabet\n')
	print word
	if dic.has_key(word):
		print '%r' ("The word is correct")
	elif editsDicFirst.has_key(word):	
		print editsDicFirst[word]

init('cut_test.txt')
