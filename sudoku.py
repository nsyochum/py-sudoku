import sys
from grid import Grid

file = str(sys.argv)
puzzle = Grid()
puzzle.parse_file(file)

# 00 01 02 03 04 05 06 07 08 09
# 10 11 12 13 14

def solve(grid):
    for row in range(9):
        for col in range(9):
            if grid.get_square(row, col) == 0:
                for num in range(1,10,1):
                    if grid.is_valid(row, col, num):
                        grid.set_square(row, col, num)
                        if solve(grid):
                            return True
                        else:
                            grid.set_square(row, col, 0)

                return False
    return True
