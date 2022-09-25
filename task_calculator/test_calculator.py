import unittest
from calculator import Calculator as Calc


class TestCalculator(unittest.TestCase):
	def test_run(self):
		self.assertEqual(Calc.run('2 + 3'), 5)
		self.assertEqual(Calc.run('+2 + +3'), 5)
		self.assertEqual(Calc.run('+2.0 + 3'), 5.0)
		self.assertEqual(Calc.run('-2 + -3'), -5)
		self.assertEqual(Calc.run('-2.0 + 3.0'), 1.0)
		self.assertEqual(Calc.run('2 * 8'), 16)
		self.assertEqual(Calc.run('100,0 / -25'), -4.0)
		self.assertEqual(Calc.run('0.75 + 0.25'), 1.0)
		self.assertEqual(Calc.run('2.9 + 0.1'), 3.0)
		self.assertEqual(Calc.run('-1000 + 1000'), 0)
		self.assertEqual(Calc.run('-0,1 - -1,1'), 1.0)
