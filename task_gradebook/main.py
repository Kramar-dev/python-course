from gradebook import Gradebook
from student import Student


def main():
	gradebook = Gradebook()
	student_1 = Student("Pinocchio")
	student_2 = Student("Timon")
	student_3 = Student("Pumba")
	
	gradebook.add_student(student_1)
	gradebook.add_student(student_2)
	gradebook.add_student(student_3)
	
	gradebook.add_mark(student_1, 3)
	gradebook.add_mark(student_1, 4)
	gradebook.add_mark(student_1, 5)
	
	gradebook.add_mark(student_2, 7)
	gradebook.add_mark(student_2, 8)
	gradebook.add_mark(student_2, 9)
	
	gradebook.add_mark(student_3, 1)
	gradebook.add_mark(student_3, 2)
	gradebook.add_mark(student_3, 3)
	gradebook.add_mark(student_3, 3)
	gradebook.add_mark(student_3, 3)
	gradebook.add_mark(student_3, 3)
	
	# gradebook.print_as_table()
	
	gradebook.get_average_mark(student_1)
	gradebook.remove_student(student_1)


if __name__ == '__main__':
	main()
