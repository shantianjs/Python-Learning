import sqlite3
import csv

connect = sqlite3.connect('data-dev.sqlite')
cursor = connect.cursor()

#获取全部表名
sqkstr = "SELECT name FROM sqlite_master WHERE type='table';"
cursor.execute(sqkstr)
tables = []
for row in cursor.fetchall():
	tables.append(row[0])

#将抬头和表写入csv
for table in tables:
	cursor.execute(f'pragma table_info({table})')
	title = list(list(zip(*cursor.fetchall()))[1])
	# title = str(title).replace(']','').replace('[','').replace('\'','\"').split()
	# title =('"'+'" "' .join(title)+'"').split()
	print(title)
	with open(f'/tem/{table}.csv','w',newline='') as fd:
		csc_writer = csv.writer(fd)
		csc_writer.writerow(title)
		cursor.execute(f'select * from {table}')
		for element in cursor.fetchall():
			csc_writer.writerow(element)


