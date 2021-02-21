"""All columns same max. Spring 2020 final exam problem.
For full credit, this must be solved without
creating new lists. Partial credit for solutions
that create new lists.

You may optionally write additional methods
or functions to break the problem down.
"""

from typing import List

class Grid(object):
    def __init__(self, grid_values: List[List[int]]):
        self._gv = grid_values

    def column_max(self, column: int) -> int:
        """one column max"""

        max = self._gv[0][column]   # initialize max in case of negative values
        for row in self._gv:
            if row[column] > max:
                max = row[column]
        return max

    def all_columns_same_max(self) -> bool:
        """all columns same max"""

        if len(self._gv) == 0:  # vacuous case for whole grid
            return True
        if len(self._gv[0]) == 1:   # vacuous case when only one row in grid
            return True
        init_max = self.column_max(0)    # base case
        for column in range(len(self._gv[0])):  # detect change in column max
            col_max = self.column_max(column)
            if col_max != init_max:
                return False
        return True
