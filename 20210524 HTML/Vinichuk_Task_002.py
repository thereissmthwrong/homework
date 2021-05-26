import sqlite3
con = sqlite3.connect('places.sqlite')
cur = con.cursor()

f = open('top13_table.html', 'a', encoding='utf-8')
f.write('''<table cellspacing="2" border="1" cellpadding="5">
<caption>Журнал посещений</caption>
<tr>
<th><font color="red">Время посещения</font></th>
<th><font color="navy">Ссылка</font></th>
</tr>
''')

for row in cur.execute('SELECT datetime(h.visit_date/1000000 - 11644473600, "unixepoch"), p.url, p.title FROM moz_historyvisits h INNER JOIN moz_places p ON p.id = h.place_id ORDER BY h.visit_date DESC LIMIT 13;'):
	f.write(f'<tr><td>{row[0]}</td><td><a href="{row[1]}">{row[2]}</a></td></tr>\n')

f.write('''</table>
</body>
''')
f.close()

