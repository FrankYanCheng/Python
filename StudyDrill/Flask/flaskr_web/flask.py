#-coding:utf-8
import sqlite3
import MySQLdb
#from flask import Flask,request,session,g,redirect,url_for,\
	#abort,render_template,flash

#app=Flask(__name__)
#app.config.from_object(__name__)

def connect_db():
	self.conn=MySQLdb.connect(host="localhost",user="root",passwd="fyc6829097", db="python_web_db",charset='utf8')
	self.cursor=conn.cursor()
	

def sql_read(sql):
	self.cursor.execute(sql)
	return cursor.fetchall()

connect_db()
print  sql_order('select * from test_table')
	
