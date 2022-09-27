import unittest
from gradebook import Gradebook
from student import Student


class TestGradebook(unittest.TestCase):
	diary = Gradebook()
	student_1 = Student("Jackie Chan")
	student_2 = Student("Bruce Lee")
	student_3 = Student("Arnold Schwarzenegger")

	def test_add_remove_student(self):
		self.diary.add_student(self.student_1)
		self.diary.add_student(self.student_2)
		self.diary.add_student(self.student_3)
		self.assertEqual(self.diary.size(), 3)
		self.diary.remove_student(self.student_1)
		self.assertEqual(self.diary.size(), 2)
		self.diary.remove_student(self.student_2)
		self.assertEqual(self.diary.size(), 1)
		self.diary.remove_student(self.student_3)
		self.assertEqual(self.diary.size(), 0)

	def test_add_mark(self):
		self.diary.add_student(self.student_1)
		self.diary.add_student(self.student_2)
		self.diary.add_student(self.student_3)
		self.diary.add_mark(self.student_1, 3)
		self.diary.add_mark(self.student_1, 4)
		self.diary.add_mark(self.student_1, 5)
		self.assertEqual(self.diary.get_average_mark(self.student_1), 4)
