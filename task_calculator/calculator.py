import re


class Calculator:
	@classmethod
	def run(cls, data):
		data = data.replace(',', '.')
		data = cls.__extract(data)
		if len(data) == 0:
			return ''
		values = cls.__parse(data)
		value_1 = values[0]
		value_2 = values[1]

		match cls.__action:
			case '+':
				return cls.__plus(value_1, value_2)
			case '-':
				return cls.__minus(value_1, value_2)
			case '*':
				return cls.__mult(value_1, value_2)
			case '/':
				return cls.__div(value_1, value_2)
		return None

	__action: str

	@classmethod
	def __plus(cls, value_1, value_2):
		return value_1 + value_2

	@classmethod
	def __minus(cls, value_1, value_2):
		return value_1 - value_2

	@classmethod
	def __mult(cls, value_1, value_2):
		return value_1 * value_2

	@classmethod
	def __div(cls, value_1, value_2):
		if value_2 == 0:
			return ZeroDivisionError
		return value_1 / value_2

	@classmethod
	def __parse(cls, data):
		lst = str(data).split(sep=' ')
		cls.__action = lst[1]
		values = [cls.__to_number(lst[0]), cls.__to_number(lst[2])]
		return values

	@classmethod
	def __to_number(cls, value):
		if '.' in value:
			return float(value)
		return int(value)

	@classmethod
	def __extract(cls, data):
		try:
			matched = re.match(r'^[+\-]?[\d.]{1,}[ ]{1}[\-+*\/]{1}[ ]{1}[+\-]?[\d.]{1,}$', data)
			return data[matched.start():matched.end()]
		except:
			return ''
