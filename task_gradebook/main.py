from gradebook import Gradebook
from student import Student


def main():
	diary = Gradebook()
	student = Student("Pinocchio")
	diary.add_student(student)
	diary.add_mark(student, 3)
	diary.get_average_mark(student)
	diary.remove_student(student)


if __name__ == '__main__':
	main()