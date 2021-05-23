import sqlite3
con = sqlite3.connect('chinook.db')
cur = con.cursor()

#распечататывают все записи из таблицы customers
def all_customers():
	print('____'*25, 'все записи из таблицы customers:', '____'*25, sep='\n')
	for row in cur.execute('SELECT * FROM customers;'):
		print(row)

#делают выборку из таблицы customers, которая выводит последовательно всех клиентов, отсортированных по имени, которые живут в Индии и сохраняют их в файл India.txt
def India_customers_by_names():
	print('____'*25, 'все записи из таблицы customers, отсортированных по имени, которые живут в Индии:', '____'*25, sep='\n')
	f = open('India.txt', 'a', encoding='utf-8')
	for row in cur.execute('SELECT * FROM customers WHERE Country = "India" ORDER BY FirstName;'):
		f.write(str(row) + '\n')
		print(row)
	f.close()

#делают выборку из таблицы customers, которая выводит последовательно всех клиентов, отсортированных по фамилии, которые живут в Бразилии и сохраняют их в файл Brazil.txt
def Brazil_customers_by_last_names():
	print('____'*25, 'все записи из таблицы customers, отсортированных по фамилии, которые живут в Бразилии:', '____'*25, sep='\n')
	f = open('Brazil.txt', 'a', encoding='utf-8')
	for row in cur.execute('SELECT * FROM customers WHERE Country = "Brazil" ORDER BY LastName;'):
		f.write(str(row) + '\n')
		print(row)
	f.close()

#делают выборку из таблицы customers, которая выводит последовательно всех клиентов, отсортированных по CustomerId, которые живут в Бразилии или Индии и сохраняют их в файл All_Customers_India_and_Brazil.txt
def India_Brazil_customers_by_CustomerId():
	print('____'*25, 'все записи из таблицы customers, отсортированных по CustomerId, которые живут в Бразилии или Индии:', '____'*25, sep='\n')
	f = open('All_Customers_India_and_Brazil.txt', 'a', encoding='utf-8')
	for row in cur.execute('SELECT * FROM customers WHERE Country = "Brazil" OR Country = "India" ORDER BY CustomerId;'):
		f.write(str(row) + '\n')
		print(row)
	f.close()

#сохраняет список клиентов и менеджеров, которые их обслуживают в файл spravochnik.txt
def all_customers_and_managers():
	print('____'*25, 'список клиентов и менеджеров, которые их обслуживают:', '____'*25, sep='\n')
	f = open('spravochnik.txt', 'a', encoding='utf-8')
	for row in cur.execute('SELECT (c.FirstName || " " || c.LastName) as Customer, (m.FirstName || " " || m.LastName) as Manager FROM customers c LEFT JOIN employees m on c.CustomerId = m.EmployeeId;'):
		f.write(str(row) + '\n')
		print(row)
	f.close()

all_customers()
India_customers_by_names()
Brazil_customers_by_last_names()
India_Brazil_customers_by_CustomerId()
all_customers_and_managers()
