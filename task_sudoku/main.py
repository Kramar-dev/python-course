from logger import Log
from game import *


def main():
	# lst = [['Francis', 'English', 453],
	#        ['Larry', 'Maths', 343],
	#        ['Nicole', 'Biology', 234],
	#        ['Joey', 'Physics', 234],
	#        ['Sam', 'Computing', 12]
	#        ]
	#
	# print("| First Name | Subject Chosen | Score |")
	# for item in lst:
	# 	print('|',
	# 	      item[0],
	# 	      " " * (9-len(item[0])),
	# 	      '|',
	# 	      item[1],
	# 	      " " * (13-len(item[1])),
	# 	      '|',
	# 	      item[2],
	# 	      " " * (4-len(str(item[2]))),
	# 	      '|'
	# 	)
	game = Game()
	game.start_new_game()


if __name__ == '__main__':
	main()

	
	

"""
sudoku create
table create
table fill randomly


while True
	print current table -> clear screen
	input: enter coordinated and value
	if value is correct --> if not existsInRow and not existsInCol and not existsInSquare
		updateTable(coordinates, value)
		continue
	else
		print invalid value
	
	keyboard interrupt exception for exit

"""
