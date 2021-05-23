import sqlite3
con = sqlite3.connect('places.sqlite')
cur = con.cursor()

#таблица всех визитов на сайты в формате: url, title, datetime
cur.execute('CREATE TABLE visits (url, title, time)')
sql = "insert into visits values(?, ?, ?)"
res=[]
for row in cur.execute('SELECT p.url, p.title, datetime(h.visit_date/1000000 - 11644473600, "unixepoch") FROM moz_historyvisits h INNER JOIN moz_places p ON p.id = h.place_id;'):
	res.append(row)
for line in res:
	cur.execute(sql, (line[0], line[1], line[2]))
for row in cur.execute('SELECT * from history;'):
	print(row)
