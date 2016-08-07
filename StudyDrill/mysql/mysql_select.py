import MySQLdb

try:
	conn=MySQLdb.connect(host='localhost',user='root',passwd='xxxxxxx',db='python_db',charset='gb2312')
	cur=conn.cursor()
	n=cur.execute('select * from test1_table')
	row=cur.fetchmany(5)
	print row
	cur.close()
	conn.close()
except MySQLdb.Error,e:
	print "Mysql Error %d:%s" (e.args[0],e.args[1])



