import calendar

class Mathematician:
	def square_nums(self, lis):
		lis = [i ** 3 for i in lis]
		return lis
	def remove_positives(self, lis):
		for i in lis:
			if i > 0:
				lis.remove(i)
		return lis
	def filter_leaps(self, lis):
		lis1 = []
		for i in lis:
			if calendar.isleap(i):
				lis1.append(i)
		return lis1
'''
m = Mathematician()

assert (m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]), "Проблема с квадратами в списке"
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
'''
