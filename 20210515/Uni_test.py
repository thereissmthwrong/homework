import unittest
from Mathematician import Mathematician

class Test_from_Assert(unittest.TestCase):
	
	def test_square_nums_TC001(self):
		self.assertTrue(m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16])
	def test_square_nums_TC002(self):
		self.assertEqual(m.square_nums([7, 11, 5, 4]), [49, 121, 25, 16])
	def test_square_nums_TC003(self):
		self.assertNotEqual(m.square_nums([7, 11, 5, 4]), [49, 121, 25, 16])
		
	def test_remove_positives_TC001(self):
		self.assertTrue(m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90])
	def test_remove_positives_TC002(self):
		self.assertEqual(m.remove_positives([26, -11, -8, 13, -90]), [-11, -8, -90])
	def test_remove_positives_TC003(self):
		self.assertNotEqual(m.remove_positives([26, -11, -8, 13, -90]), [11, -8, -90])
		
	def test_filter_leaps_TC001(self):
		self.assertTrue(m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020])
	def test_filter_leaps_TC002(self):
		self.assertEqual(m.filter_leaps([2001, 1884, 1995, 2003, 2020]), [1884, 2020])
	def test_filter_leaps_TC003(self):
		self.assertNotEqual(m.filter_leaps([2001, 1884, 1995, 2003, 2020]), [2020, 1884])

if __name__ == '__main__':
	m = Mathematician()
	unittest.main()
