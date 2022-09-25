from student import Student


class Diary:
	def add_student(self, student: Student):
		self.__diary[student.get_name()] = []

	def add_mark(self, student: Student, mark: int):
		self.__diary[student.get_name()].append(mark)

	def remove_student(self, student: Student):
		del self.__diary[student.get_name()]

	def get_average_mark(self, student: Student):
		total = 0
		marks = self.__diary[student.get_name()]
		for index, mark in enumerate(marks):
			total += mark
		return total/len(marks)

	def size(self):
		return len(self.__diary)

	__diary = {}
