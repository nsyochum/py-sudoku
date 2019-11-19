import sys
import matplotlib.pyplot as plt

from grid import Grid


def solve(grid):
    for row in range(9):
        for col in range(9):
            if grid.get_square(row, col) == 0:
                for num in range(1, 10, 1):
                    if grid.is_valid(row, col, num):
                        grid.set_square(row, col, num)
                        if solve(grid):
                            return True
                        else:
                            grid.set_square(row, col, 0)
                return False
    return True


file = str(sys.argv[1])
puzzle = Grid()
puzzle.parse_file(file)
puzzle.print_grid()
solve(puzzle)
puzzle.print_grid()
