import json
import sqlite3

db=sqlite3.connect("Task1.db")
from pprint import pprint
json_data=open('data.json')
with db:
	cur=db.cursor()
	cur.execute('DROP TABLE IF EXISTS demodetails1')
	cur.execute('CREATE TABLE  demodetails1(demoid INTEGER,demoname TEXT NOT NULL,description TEXT NOT NULL,device_details TEXT NOT NULL,status  INTEGER NOT NULL DEFAULT 0)')

data = json.load(json_data)
#Printing only value 
for key in data:
	for key1 in data[key]:
		#this has a hash
	 	for actual_key in key1:
			if actual_key == 'demoid':
				demoid_value = key1[actual_key]
			elif actual_key == 'demoname':
				demonname_value = key1[actual_key]
			elif actual_key == 'description':
				description_value = key1[actual_key]
			elif actual_key == 'device_details':
				device_details_value = key1[actual_key]
		cur.execute('INSERT INTO demodetails1(demoid,demoname,description,device_details,status) VALUES (?,?,?,?,0)',[demoid_value,demonname_value,description_value,device_details_value])
json_data.close()
db.close()	         
