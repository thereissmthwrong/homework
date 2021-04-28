import sys

inp = sys.argv[1:]

h = """This calculator needs the following syntax: <value> <value> ... <value> <operation>.
For example: 5 5 1 -. The calculation logic is the following: 5-5-1=-1.
Available keys:
-h help
-v print result with formula (e.g. 5 5 1 + -v)
-f <file name> copy result in a file (e.g. 5 5 1 + -f "result")"""

def get_formula(m):
	operation = m[-1]
	m.pop()
	formula = m[0]

	for i in m[1:]:
		formula += str(operation) + str(i)
	
	return formula

def export_to_file(f_name, n):
	f = open(f'{str(f_name)}.txt', 'w', encoding='utf-8')
	f.write(str(eval(n)))
	f.close()

if inp[0].isnumeric():
	if inp[-1] == '-v':
		form = get_formula(inp[:-1])
		print(f'{form}={eval(form)}')
	elif inp[-2] == '-f':
		form = get_formula(inp[:-2])
		export_to_file(inp[-1], form)
		print(eval(form))
	else:
		print(eval(get_formula(inp)))
elif inp[0] == '-h':
	print(h)

