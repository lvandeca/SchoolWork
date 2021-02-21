"""Unit tests for all_columns_same_max"""

import unittest
from q4_col_max_same import Grid

class Test_0_Basic(unittest.TestCase):
    """Pass these tests first"""

    def test_0_empty(self):
        """Empty grid case"""
        grid = Grid([])
        self.assertTrue(grid.all_columns_same_max())

    def test_1_1x1(self):
        """One row, one column"""
        grid = Grid([[32]])
        self.assertTrue(grid.all_columns_same_max())

    def test_2_1x2(self):
        """If there's only one column, it must be the same"""
        grid = Grid([[-12],
                     [24]])
        self.assertTrue(grid.all_columns_same_max())

    def test_3_2x1_t(self):
        """Two columns, one row, same"""
        grid = Grid([[12, 12]])
        self.assertTrue(grid.all_columns_same_max())

    def test_4_2x1_f(self):
        """Two columns, one row, not same"""
        grid = Grid([[14, 12]])
        self.assertFalse(grid.all_columns_same_max())

    def test_5_typical_t(self):
        """A typical grid with equal max columns"""
        grid = Grid([[10, 15, 20],
                     [5, 20, 13],
                     [20, 5, 8]])
        self.assertTrue(grid.all_columns_same_max())

    def test_6_typical_f(self):
        """Cols not equal, rows equal"""
        grid = Grid([[10, 15, 20],
                     [20, 15, 20],
                     [20, 13, 10]])
        self.assertFalse(grid.all_columns_same_max())

    def test_7_wide_t(self):
        """Wide shallow grid, even"""
        grid = Grid([[10, 20, 10, 20, 10],
                     [20,  5, 20, 20, 20]])
        self.assertTrue(grid.all_columns_same_max())

    def test_8_wide_f(self):
        """Wide shallow grid, imbalanced columns"""
        grid = Grid([[10, 20, 10, 20, 10],
                     [20, 10, 20, 20, 10]])
        self.assertFalse(grid.all_columns_same_max())

    def test_9_tall_t(self):
        """Tall narrow grid, balanced"""
        grid = Grid([[10, 5],
                     [5, 5],
                     [8, 7],
                     [4, 10],
                     [6, 3]])
        self.assertTrue(grid.all_columns_same_max())

    def test_10_tall_f(self):
        """Tall narrow grid, imbalanced"""
        grid = Grid([[10, 5],
                     [10, 5],
                     [8, 7],
                     [10, 5],
                     [6, 3]])
        self.assertFalse(grid.all_columns_same_max())

class Test_1_ErrorBased(unittest.TestCase):
    """Some test cases based on anticipated errors"""

    def test_0_neg_max_t(self):
        """Max of negative numbers is a negative number"""
        grid = Grid([[-9995, -9998, -9993],
                     [-9993, -9998, -9993],
                     [-9998, -9993, -9998]])
        self.assertTrue(grid.all_columns_same_max())

    def test_1_neg_max_f(self):
        """Max of negative numbers is negative number"""
        grid = Grid([[-9995, -9998, -9993],
                     [-9993, -9990, -9993],
                     [-9998, -9993, -9998]])
        self.assertFalse(grid.all_columns_same_max())

    def test_2_no_clobber(self):
        """Method should not make undocumented modifications
        to the state of the object."""
        # How can we check this
        # without looking inside?  Maybe we'll peek.
        # Sometimes test cases have to bend the rules.
        grid = Grid([[10, 5],
                     [10, 5],
                     [8, 7],
                     [10, 5],
                     [6, 3]])
        check = grid.all_columns_same_max()
        self.assertEqual(grid._gv,
                         [[10, 5],
                          [10, 5],
                          [8, 7],
                          [10, 5],
                          [6, 3]]
                         )

if __name__ == "__main__":
    unittest.main()










