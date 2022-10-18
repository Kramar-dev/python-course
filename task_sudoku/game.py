import types
import os
from sudoku import *

defines = types.SimpleNamespace()
defines.NEW_GAME = 101
defines.INVALID = -1
defines.EXIT = -2
defines.HELP = 100
defines.GAME_HELP_INFO = """
+--------------------------------------------------------------------
|
| E - exit
| G - new game
| N - help me and enter next value instead of me =)
| F - sorry, I am a looser, fill whole table instead of me
| XY V - value for enter in table
|   where:
|       X - x-axis coordinate
|       Y - y-axis coordinate
|       V - value to enter in table (0-9)
|
+--------------------------------------------------------------------
"""


class Game:
	def __init__(self):
		pass

	__sudoku: Sudoku

	def __cls(self):
		os.system('cls')  # print("\033[H\033[J", end="")

	def start_new_game(self):
		self.__create_table()
		while True:
			try:
				self.__cls()
				print('\n')
				self.__show_current_table()
				user_input = int(self.__get_user_input())
				match user_input:
					case defines.EXIT:
						Game.__exit_game()
					case defines.NEW_GAME:
						self.start_new_game()
					case defines.INVALID:
						Game.__show_game_help()
						continue
					case defines.HELP:
						Game.__show_game_help()
						continue
				self.__update_table(user_input)
			except KeyboardInterrupt:
				self.__exit_game()

	@staticmethod
	def __exit_game():
		exit(0)

	def __get_user_input(self):
		user_input = input('\nEnter command:\n (H - help)\n')
		user_input = user_input.lower()
		try:
			if len(user_input) != 4:
				return defines.INVALID
			x = user_input[0]
			y = user_input[1]
			v = user_input[3]

			as_int_x = int(x)
			as_int_y = int(y)
			as_int_v = int(v)
			if as_int_x not in range(9):
				return defines.INVALID
			if as_int_y not in range(9):
				return defines.INVALID
			if as_int_v not in range(9):
				return defines.INVALID
			return int(f'{x}{y}{v}')
		except:
			if user_input == 'h':
				return defines.HELP
			if user_input == 'e':
				return defines.EXIT
		return defines.INVALID

	@staticmethod
	def __show_game_help():
		print(defines.GAME_HELP_INFO)

	def __show_invalid_input(self):
		self.__show_game_help()

	def __generate_next_value(self):
		pass

	def __create_table(self):
		self.__sudoku = Sudoku(9)

	def __update_table(self, update):
		x = str(update)[0]
		y = str(update)[1]
		v = str(update)[2]
		self.__sudoku.update_table(int(x), int(y), int(v))

	def __show_current_table(self):
		self.__sudoku.print_current_table()
