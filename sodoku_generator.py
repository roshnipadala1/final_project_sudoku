import random

class SudokuGenerator:
    def __init__(self, row_length=9, cells):
        self.row_length = row_length
        self.cells = cells
        self.board = []
        for i in range(row_length):
            row = []
            for j in range(row_length):
                row.append(0)
            self.board.append(row)
    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:
            line = ""
            for i in row:
                if i == 0:
                    value = " "
                else:
                    value = str(i)
                line += value + " "
            print(line)

    def valid_in_row(self,row, num):
        return num not in self.board[row]
    def valid_in_col(self, col, num):
        for i in range(self.row_length):
            if self.board[i][col] == num:
                return False
        return True
    def valid_in_box(self, row_start, col_start, num):
        for i in range(row_start, row_start+3)
            for j in range(col_start, col_start+3)
                if self.board[i][j] == num:
                    return False
        return True
    def is_valid(self, row, col, num):
        if not self.valid_in_row(row,num):
            return False
        if not self.valid_in_col:
            return False
        if not self.valid_in_box:
            return False
        return True
    def fill_box(self, row_start, col_start):
        nums = list(range(1,10))
        random.shuffle(nums)
        num = 0
        for i in range(row_start, row_start+3):
            for j in range(col_start, col_start+3):
                self.board[][j] = nums[num]
                num +=1

    def fill_diagonal(self):

    def fill_remaining(self):

    def fill_values(self):

    def remove_cells(self):

