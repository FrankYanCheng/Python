import MySQLdb

try:
	conn=MySQLdb.connect(host='localhost',user='root',passwd='fyc6829097')
	conn.select_db("python_web_db")
	cur=conn.cursor()
	
	value=['title','Roln']
	cur.execute('insert into test_table(title,content) values(%s,%s)',value)
	conn.commit()
	cur.close()
	conn.close()
except MySQLdb.Error,e:
	print "Mysql Error %d: %s" %(e.args[0],e.args[1])
