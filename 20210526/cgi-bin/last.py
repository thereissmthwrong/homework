#!/usr/bin/env py

import sqlite3

print("Content-type: text/html")
print("Cache-Control: no-cache")
print()

print('''
<!DOCTYPE html>
<html class="client-nojs" lang="ru" dir="ltr">
<head>
<meta charset="UTF-8"/>''')
print('''
<body>''')

con = sqlite3.connect(r'C:\Users\QA\Desktop\Homework\20210526\cgi-bin\places.sqlite')
cur = con.cursor()

for row in cur.execute('SELECT datetime(h.visit_date/1000000 - 11644473600, "unixepoch"), p.url, p.title FROM moz_historyvisits h INNER JOIN moz_places p ON p.id = h.place_id ORDER BY h.visit_date DESC LIMIT 13;'):
	print(f'<li>{row[0]} <a href="{row[1]}">{row[2]}</a></li>\n')

print('''
</body>
</html>''')
