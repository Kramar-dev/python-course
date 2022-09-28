from student import Student


class Gradebook:
	def add_student(self, student: Student):
		self.__diary[student] = []

	def add_mark(self, student: Student, mark: int):
		self.__diary[student].append(mark)

	def remove_student(self, student: Student):
		del self.__diary[student]

	def get_average_mark(self, student: Student):
		total = 0
		marks = self.__diary[student]
		for index, mark in enumerate(marks):
			total += mark
		return total/len(marks)

	def size(self):
		return len(self.__diary)

	def print_as_table(self):  # TODO sometimes...
		number_header = 'NR'
		name_header = 'NAME'
		marks_header = 'MARKS'
		average_header = 'AVERAGE'
		template = "{:^%d}\t\t{:^%d}\t\t\t{:^%d}\t\t\t{:^%d}" % (len(number_header), len(name_header), len(marks_header), len(average_header))
		print(template.format(number_header, name_header, marks_header, average_header))
		nr = 1
		for key, value in self.__diary.items():
			average = self.get_average_mark(key)
			tmp = "{:^%d}\t\t{:^%d}\t\t\t{:^%d}\t\t\t{:^%d}" % (len(str(nr)), len(key.name), len(str(value)), len(str(average)))
			print(tmp.format(nr, key.name, str(value), average))
			nr += 1

	__diary = {}
	