#!/home/karthik/Latest/new/bin/python 

import sqlite3

db=sqlite3.connect("Task.db")

with db:
	cur=db.cursor()
	res = cur.execute('select userid,demoname from demo_user_table where strftime("%Y-%m-%d %H:%M","now","localtime") > strftime("%Y-%m-%d %H:%M","+1 Hour",duration) and demo_status =1 ')
	list_value = [dict(demoid=row[0],demoname=row[1]) for row in res.fetchall()]
	if len(list_value)>0:
	    for value in list_value:
	        cur.execute('delete from demo_user_table where userid=?,demoname=?',[value['userid'],value['demoname']])
		cur.execute('update demodetails set status=0 where demoname =?',[value['demoname']])
		cur.execute('insert into lab_history(userid,demoname,booked_time,status) values ("System",?,strftime("%Y-%m-%d %H:%M","now","localtime"),0)',[value['demoname']])		
db.commit()	
db.close()	         
