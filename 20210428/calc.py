import sys
import argparse

parser = argparse.ArgumentParser(description='Four actions calculator')

parser.add_argument('x', type=float, nargs='+', help='arguments')
parser.add_argument('op', choices=['+','-','*','/'], help='operation')
parser.add_argument('--verbose','-v', action='store_true', help='print result with formula (e.g. 5 5 1 + -v)') # печатать не просто ответ, а выражение целиком
parser.add_argument('--file','-f', action='store_true', help='copy result in a file (e.g. 5 5 1 + -f "result")') # сбрасываем результат файл
parser.add_argument('--quiet','-q', action='store_true', help='the result is not shown but can be saved into a file') # вывод на экран не должен происходить (но может сохраняться в файл, если он задан)
parser.add_argument('--append','-a', action='store_true', help='copy result in a file via appending a new result line') # файл не должен затираться, а вместо этого - дописываться.

args = parser.parse_args(sys.argv[1:])

def get_formula(args,op):
	formula = f'{args[0]} '
	for i in args[1:]:
		formula += f'{op} {i} '
	return formula + '='

def export_to_file(f_name, r, is_app):
	if is_app:
		f = open(f'{str(f_name)}.txt', 'a', encoding='utf-8')
	else:
		f = open(f'{str(f_name)}.txt', 'w', encoding='utf-8')
	f.write(str(r)+'\n')
	f.close()

r = 0

if args.op == '+':
	for i in args.x:
		r += i
elif args.op == '-':
	r = args.x[0]
	for i in args.x[1:]:
		r -= i
elif args.op == '*':
	r = args.x[0]
	for i in args.x[1:]:
		r *= i
elif args.op == '/':
	r = args.x[0]
	for i in args.x[1:]:
		r /= i

if args.file:
	if args.append:
		export_to_file('Results',r,True)
	else:
		export_to_file('Results',r,False)
	if args.quiet:
		pass
	else:
		if args.verbose:
			print(get_formula(args.x,args.op),r)
		else:
			print(r)
elif args.quiet:
	pass
else:
	if args.verbose:
		print(get_formula(args.x,args.op),r)
	else:
		print(r)

