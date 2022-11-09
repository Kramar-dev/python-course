import sys
name = str(__file__)
index = name.index('\\task_sudoku\sudoku.py') + 1
sys.path.insert(1, name[:index])


import types
from logger import Log
import random as rnd
from ansicolors import Colors


class Sudoku:
    mode = types.SimpleNamespace()
    mode.PREPARE = 0
    mode.GAME = 1
    
    def __init__(self, size):
        self.size = size + 1
        self.table = []
        self.busy_cell_count = 0
        self.mode = Sudoku.mode.PREPARE
        self.create_table()
        self.fill_table_by_empty()
        self.fill_table()
        self.mode = Sudoku.mode.GAME

    def create_table(self):
        for row in range(self.size):
            self.table.append([])
        num = 0

        for row in range(self.size):
            self.table[row].append(f'{num}')
            num += 1

        num = 1
        for col in range(self.size - 1):
            self.table[0].append(f'{num}')
            num += 1

        self.table[0][0] = ' '

    def fill_table_by_empty(self):
        for y in range(self.size - 1):
            for x in range(self.size - 1):
                self.table[y + 1].append('[ ]')

    def print_current_table(self):
        table_head_row = '   '

        for x in range(1, self.size):
            table_head_row += f'[{self.table[0][x]}]'
        Log.w(table_head_row)

        for y in range(1, self.size):
            current_line = f'[{Colors.YELLOW}{self.table[y][0]}]{Colors.END}'
            for x in range(1, self.size):
                sq_number_x = self.get_square_number(x)
                sq_number_y = self.get_square_number(y)
                div_x, mod_x = divmod(sq_number_x, 2)
                div_y, mod_y = divmod(sq_number_y, 2)
                if mod_x == mod_y:
                    current_line += f'{Colors.LIGHT_CYAN}{self.table[y][x]}{Colors.END}'
                else:
                    current_line += f'{Colors.LIGHT_GREEN}{self.table[y][x]}{Colors.END}'
                #current_line += self.table[y][x]
            Log.w(current_line)

    def update_table(self, x, y, value):
        if self.can_update(x, y, value):
            self.table[y][x] = f'[{value}]'
            self.busy_cell_count += 1
            if self.busy_cell_count == 89:
                Log.i("You won!")
                exit(0)


    def exists_in_row(self, x, y, value):
        counter = 0
        for element in self.table[y]:
            if counter == 0:
                counter += 1
                continue
            if element == f'[{value}]':
                return True
            counter += 1
        return False

    def exists_in_col(self, x, y, value):
        counter = 0
        for row in self.table:
            if counter == 0:
                counter += 1
                continue
            if row[x] == f'[{value}]':
                return True
            counter += 1
        return False

    def exists_in_square(self, x, y, value):
        square_x = self.get_square_number(x)
        square_y = self.get_square_number(y)
        square_list = self.get_mini_list(square_x, square_y)
        if f'[{value}]' in square_list:
            return True
        return False

    def get_square_number(self, value):
        div, mod = divmod(value, 3)
        if mod == 0:
            return div
        return div + 1

    def get_mini_list(self, x_sq, y_sq):
        mini_list = []
        for y_ in reversed(range(3)):
            for x_ in reversed(range(3)):
                xx = 3 * x_sq - y_
                yy = 3 * y_sq - x_
                mini_list.append(self.table[yy][xx])
        return mini_list

    def can_update(self, x, y, value) -> bool:
        if self.cell_busy(self.table[y][x]):
            if self.mode == Sudoku.mode.GAME:
                Log.w("Sorry, this cell is busy")
            return False
        if self.exists_in_row(x, y, value):
            if self.mode == Sudoku.mode.GAME:
                Log.e(f"Sorry, element already exists in current row {y}")
            return False
        if self.exists_in_col(x, y, value):
            if self.mode == Sudoku.mode.GAME:
                Log.e(f"Sorry, element already exists in current column {x}")
            return False
        if self.exists_in_square(x, y, value):
            if self.mode == Sudoku.mode.GAME:
                Log.e(f"Sorry, element already exists in current square")
            return False
        return True
        
    def cell_busy(self, element):
        for number in range(1, 10):
            if str(number) in element:
                return True
        return False

    def fill_next_random_cell(self):
        x = rnd.randint(1, 9)
        y = rnd.randint(1, 9)
        value = rnd.randint(1, 9)
        self.update_table(x, y, value)
        pass

    def fill_table(self):
        while self.busy_cell_count < 27:
            self.fill_next_random_cell()
