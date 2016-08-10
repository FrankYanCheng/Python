import MySQLdb
from flask import Flask,request,session,g,redirect,url_for,abort,render_template,flash
import datetime
SECRET_KEY='key'
USERNAME='admin'
PASSWORD='default'

app=Flask(__name__)
app.config.from_object(__name__)

def connect_db():
	conn=MySQLdb.connect(host="localhost",user="root",passwd="xxxxxxx", db="python_web_db",charset='utf8')
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

def sql_insert(sql,parameter):
	try:
		conn=connect_db()
		cursor=conn.cursor()
		cursor.execute(sql,parameter)
		conn.commit()
		cursor.close()
		conn.close()
	except MySQLdb.Error,e:
		print "Mysql Error %d:%s" %(e.args[0],e.args[1])

@app.route('/',methods=['GET','POST'])
def login():
	error=None
	if request.method=='POST':
		if request.form['username']!=app.config['USERNAME']:
			error='Invalid username!'
		elif request.form['password']!=app.config['PASSWORD']:
			error='Invalid password'
		else:
			session['logged_in']=True
			flash('You were logged in')
			return redirect(url_for('show_text'))
	return render_template('login.html',error=error)

@app.route('/text')
def show_text():
	if not session.get('logged_in'):
		abort(401)
	else:
		table=sql_read('select * from test_table')
		return render_template('show_text.html',table=table)

@app.route('/add',methods=['POST'])
def add_text():
	#sql_insert('insert into test_table (title,content) values(%s,%s)',request.form['title'],request.form['content'])
	title=request.form['title']
	content=request.form['content']
	time=datetime.datetime.now()
	value=[title,content]
	sql="insert into test_table (title,content,time) values (%s,%s,now())"
	sql_insert(sql,value)
	return redirect(url_for('show_text'))

if __name__=='__main__':
	app.run(host='fyc.pub')
#	print show_text()
