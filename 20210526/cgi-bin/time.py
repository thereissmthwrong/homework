#!/usr/bin/env py
import datetime
vrem = datetime.datetime.strftime(datetime.datetime.now(), "%Y.%m.%d %H:%M:%S")
# служебные заголовки
print("Content-type: text/html")
print("Cache-Control: no-cache")
print()
# содержимое сайта
print('''
<!DOCTYPE html>
<html class="client-nojs" lang="ru" dir="ltr">
<head>
<meta charset="UTF-8"/>''')
print('''
<body>''')
print('<title>Date and time</title>')
print(f'<h1>Current time:</h1>')
print(f'<p>{vrem}</p>')
print('''
</body>
</html>''')
