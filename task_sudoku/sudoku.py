from logger import Log
import random as rnd

class Sudoku:
    def __init__(self, size):
        self.size = size + 1
        self.table = []
        self.create_table()
        self.fill_table_by_empty()
        self.fill_table()

    def create_table(self):
        for row in range(self.size):
            self.table.append([])
        num = 0

        for row in range(self.size):
            self.table[row].append(f'{num}')
            num += 1

        num = 1
        for col in range(self.size - 1):
            self.table[0].append(f' {num} ')
            num += 1

        self.table[0][0] = ' '

    def fill_table_by_empty(self):
        for x in range(self.size - 1):
            for y in range(self.size - 1):
                self.table[x + 1].append('[ ]')

    def print_current_table(self):
        for x in range(self.size):
            # div, mod = divmod(row, self.size/3)
            # if mod == 0:
            # print('-------------------------------------------------------------')
            Log.v(self.table[x])

    def update_table(self, x, y, value):
        if self.can_update(x, y, value):
            self.table[y][x] = f'[{value}]'

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
        if value in square_list:
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
                mini_list.append(self.table[xx][yy])
        return mini_list

    def can_update(self, x, y, value) -> bool:
        if self.cell_busy(self.table[x][y]):
            #Log.w("Sorry, this cell is busy")
            return False
        if self.exists_in_row(x, y, value):
            #Log.e(f"Sorry, element already exists in current row {x}")
            return False
        if self.exists_in_col(x, y, value):
            #Log.e(f"Sorry, element already exists in current column {y}")
            return False
        if self.exists_in_square(x, y, value):
            return False
        return True
        
    def cell_busy(self, element):
        for number in range(1, 9):
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
        for i in range(30):
            self.fill_next_random_cell()
