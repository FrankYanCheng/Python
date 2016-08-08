import MySQLdb
from flask import Flask,request,session,g,redirect,url_for,abort,render_template,flash
import datetime
SECRET_KEY='key'
USERNAME='admin'
PASSWORD='default'

app=Flask(__name__)
app.config.from_object(__name__)

def connect_db():
	conn=MySQLdb.connect(host="localhost",user="root",passwd="fyc6829097", db="python_web_db",charset='utf8')
	return conn

def sql_read(sql):
	conn=connect_db()
	cursor=conn.cursor()
	cursor.execute(sql)
	table=cursor.fetchall()
	conn.commit()
	cursor.close()
	conn.close()
	return table

def sql_insert(sql):
	conn=connect_db()
	cursor=conn.cursor()
	cursor.execute(sql)
	conn.commit()
	cursor.close()
	conn.close()

@app.route('/')
def show_text():
	table=sql_read('select * from test_table')
	return render_template('show_text.html',table=table)

@app.route('/add_text',methods=['POST'])
def add_text():
#	sql_insert('insert into test_table (title,content) values(%s,%s)',request.form['title'],request.form['content'])
	return redirect(url_for('show_text'))


if __name__=='__main__':
	app.run(host='fyc.pub')
#	print show_text()
