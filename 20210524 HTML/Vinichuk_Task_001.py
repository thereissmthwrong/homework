import sqlite3
con = sqlite3.connect('places.sqlite')
cur = con.cursor()

f = open('top13.html', 'a', encoding='utf-8')
f.write('<ul>\n')

for row in cur.execute('SELECT datetime(h.visit_date/1000000 - 11644473600, "unixepoch"), p.url, p.title FROM moz_historyvisits h INNER JOIN moz_places p ON p.id = h.place_id ORDER BY h.visit_date DESC LIMIT 13;'):
	f.write(f'<li>{row[0]} <a href="{row[1]}">{row[2]}</a></li>\n')

f.write('</ul>')
f.close()

