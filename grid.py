import numpy as np
import csv


class Grid:
    """Class to handle puzzle logic"""

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
    def __init__(self):
        self.grid = np.zeros((9, 9)).astype(int)

    # sets the given location to the given number
    def set_square(self, row, col, num):
        self.grid[row, col] = num

    # returns the value at a given square
    def get_square(self, row, col):
        return self.grid[row, col]

    # this method checks if the location is a valid position for the number in the grid
    # loc: a tuple in the form of (row, col)
    # num: a number 1-9 to check
    # returns True if this is valid, false otherwise
    def is_valid(self, row, col, num):
        if (num, row, col) < (1, 0, 0) or (num, row, col) > (9, 8, 8):
            return False

        return self.check_row(num, row) and self.check_column(num, col) and self.check_square(row, col, num)

    # this method checks if the num is unique in the given row
    # num: the number to check
    # row: the row to check
    # returns True if the number is valid in the row, False otherwise
    def check_row(self, num, row):
        for number in self.grid[row, :]:
            if int(num) == int(number):
                return False

        return True

    # this method checks if the num is unique in the given column
    # num: the number to check
    # column: the column to check
    # returns True if the number is valid in the column, False otherwise
    def check_column(self, num, column):
        for number in self.grid[:, column]:
            if int(number) == int(num):
                return False

        return True

    # this method checks if the num is unique in the given square
    # num: the number to check
    # loc: the location in the square
    # returns True if the number is valid in the square, False otherwise
    def check_square(self, row, col, num):
        topRow = int(int(row / 3) * 3)
        leftCol = int(int(col / 3) * 3)
        for rowOffset in range(3):
            for colOffset in range(3):
                if int(self.grid[topRow + rowOffset, leftCol + colOffset]) == int(num):
                    return False

        return True

    # checks if the puzzle is solved
    def is_solved(self):
        small_sum = sum(range(1, 10, 1))
        puzzle_sum = small_sum * 9

        # check total sum
        total_sum = sum(self.grid)
        if total_sum != puzzle_sum:
            return False

        # check each row
        for row in range(9):
            row_sum = sum(self.grid[row, :])
            if row_sum != small_sum:
                return False

        # check each col
        for col in range(9):
            col_sum = sum(self.grid[:, col])
            if col_sum != small_sum:
                return False

        # square sum
        for col in range(3):
            for row in range(3):
                square_sum = self.sum_square(row*3, col*3)
                if square_sum != small_sum:
                    return False

        return True

    # sums over the square that starts on the given location
    def sum_square(self, row, col):
        square_sum = 0
        for col_off in range(3):
            for row_off in range(3):
                square_sum += self.grid[row + row_off, col + col_off]

        return square_sum

    # This method prints out the current grid to the console
    def print_grid(self):
        for row in range(9):
            rowBuild = ''
            for col in range(9):
                if col == 3 or col == 6:
                    rowBuild += '| '

                rowBuild += str(self.grid[row, col]) + ' '

            print(rowBuild)

            if row == 2 or row == 5:
                dashedLine = ''
                for i in range(21):
                    dashedLine += '-'

                print(dashedLine)
        print()

    # This method outputs the grid to the given file
    def print_file(self, file_name):
        with open(file_name) as csv_file:
            writer = csv.writer(csv_file)
            for row in range(9):
                row_str = ''
                for column in range(9):
                    row_str += str(self.grid[row, column])

                writer.writerow(row_str)

    # This method parses a grid from the given file
    def parse_file(self, file_name):
        with open(file_name) as csv_file:
            reader = csv.reader(csv_file)
            row_num = 0
            for row in reader:
                self.grid[row_num, :] = [int(datum) for datum in row]
                row_num += 1


