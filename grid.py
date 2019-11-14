import numpy as np


class Grid:
    # layout of the puzzle
    # row, column
    # -1 -1 -1 | -1 -1 -1 | -1 -1 -1
    # -1 00 -1 | -1 11 -1 | -1 22 -1
    # -1 -1 -1 | -1 -1 -1 | -1 -1 -1
    # ---------|----------|---------
    # -1 -1 -1 | -1 -1 -1 | -1 -1 -1
    # -1 33 -1 | -1 44 -1 | -1 55 -1
    # -1 -1 -1 | -1 -1 -1 | -1 -1 -1
    # ---------|----------|---------
    # -1 -1 -1 | -1 -1 -1 | -1 -1 -1
    # -1 66 -1 | -1 77 -1 | -1 88 -1
    # -1 -1 -1 | -1 -1 -1 | -1 -1 -1

    grid = np.ones(9, 9) * -1

    # this method checks if the location is a valid position for the number in the grid
    # loc: a tuple in the form of (row, col)
    # num: a number 1-9 to check
    # returns True if this is valid, false otherwise
    def is_valid(self, loc, num):
        row = loc[0]
        col = loc[1]

        if (num, row, col) < (1, 1, 1) or (num, row, col) > (9, 9, 9):
            return False

        return self.check_row(num, row) and self.check_column(num, col)

    # this method checks if the num is unique in the given row
    # num: the number to check
    # row: the row to check
    # returns True if the number is valid in the row, False otherwise
    def check_row(self, num, row):
        for number in self.grid[row, :]:
            if number == num:
                return False

        return True

    # this method checks if the num is unique in the given column
    # num: the number to check
    # column: the column to check
    # returns True if the number is valid in the column, False otherwise
    def check_column(self, num, column):
        for number in self.grif[:, column]:
            if number == num:
                return False

        return True

    # this method checks if the num is unique in the given square
    # num: the number to check
    # loc: the location in the square
    # returns True if the number is valid in the square, False otherwise
    def check_square(self, num, loc):
        topRow = (loc[0] / 3) * 3
        leftCol = (loc[1] / 3) * 3
        for rowOffset in range(3):
            for colOffset in range(3):
                if self.grid[topRow + rowOffset, leftCol + colOffset] == num:
                    return False

        return True
