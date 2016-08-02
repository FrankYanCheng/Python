import MySQLdb

conn=MySQLdb.connect(host="localhost",user="root",passwd="fyc6829097",db="python_db",charset="utf8")
cursor=conn.cursor()

#sql="insert into test1_table(id,name) values(%s,%s)"
#param=(123,'test')
#n=cursor.execute(sql,param)
sql="select * from test1_table"
#sql="insert into test1_table(id,name) values(1,'frank')"
n=cursor.execute(sql)
row=cursor.fetchone()
print n
print row
row=cursor.fetchone()
print row
