class Sudoku:
	def __init__(self, size):
		self.size = size + 1
		self.table = []
		self.create_table()
		self.fill_table()
		pass

	def create_table(self):
		for row in range(self.size + 1):
			self.table.append([])
		num = 0

		for row in range(self.size):
			self.table[row].append(f'{num}')
			# row.append(f' {chr(ascii)}')
			num += 1

		num = 1
		for col in range(self.size - 1):
			self.table[0].append(f' {num} ')
			num += 1

		self.table[0][0] = ' '

	def fill_table(self):
		for row in range(self.size - 1):
			# self.table.append([])
			for col in range(self.size - 1):
				self.table[row + 1].append('[ ]')
		pass

	def print_current_table(self):
		for row in range(self.size):
			# div, mod = divmod(row, self.size/3)
			# if mod == 0:
			# print('-------------------------------------------------------------')
			print(self.table[row])

	def update_table(self, x, y, value):
		self.table[x][y] = f'[{value}]'

	def existsInRow(self):
		return False

	def existsInCol(self):
		return False

	def existsInSquare(self):
		return False
