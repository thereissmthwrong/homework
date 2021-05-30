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

con = sqlite3.connect(r'C:\Users\QA\Desktop\Homework\20210526\cgi-bin\chinook.db')
cur = con.cursor()

for row in cur.execute('SELECT FirstName, LastName, Country FROM Customers;'):
	print(f'<li>{row[0]} {row[1]} - {row[2]}</li>\n')

print('''
</body>
</html>''')
