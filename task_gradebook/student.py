class Student:
	def __init__(self, name):
		self.__name: str = name

	def get_name(self) -> str:
		return self.__name

