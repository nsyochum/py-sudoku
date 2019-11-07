import numpy as np


class Grid:
    # layout of the puzzle
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

    def is_valid(self, loc, num):
        row = loc[0]
        col = loc[0]

        return

    def box_num(self, loc):
        return (loc[0] * 9 + loc[1]) / 9

    def in_box(self, loc, num):
        box = box_num(self, loc)

