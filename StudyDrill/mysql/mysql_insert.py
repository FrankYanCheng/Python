import MySQLdb

try:
	conn=MySQLdb.connect(host='localhost',user='root',passwd='xxxxxx')
	conn.select_db("python_db")
	cur=conn.cursor()
	
	value=[3,'Roln']
	cur.execute('insert into test1_table values(%s,%s)',value)
	conn.commit()
	cur.close()
	conn.close()
except MySQLdb.Error,e:
	print "Mysql Error %d: %s" %(e.args[0],e.args[1])
