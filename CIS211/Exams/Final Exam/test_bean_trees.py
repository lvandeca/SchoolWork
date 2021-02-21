""""Spring 2020 final exam, CIS 211.
Test Bertie Botts Every Flavor Bean Trees
"""

import unittest
from q1_bean_trees import *

class Test_Bean_Trees(unittest.TestCase):
    """What flavor beans are in that tree?"""

    def test_0_leaf(self):
        tree = Leaf(Flavor.cherry)
        self.assertEqual(tree.flavors(), set([Flavor.cherry]))

    def test_1_branch(self):
        l0 = Leaf(Flavor.cherry)
        l1 = Leaf(Flavor.banana)
        tree = Branch(l1, l0)
        self.assertEqual(tree.flavors(),
                         set([Flavor.banana, Flavor.cherry]))

    def test_2_bigger(self):
        l0 = Leaf(Flavor.cherry)
        l1 = Leaf(Flavor.banana)
        l2 = Leaf(Flavor.banana)
        l3 = Leaf(Flavor.dirt)
        l4 = Leaf(Flavor.earwax)
        l5 = Leaf(Flavor.cinnamon)
        tree = Branch(l0,
                      Branch(l1,
                             Branch(Branch(l2, l3),
                                    Branch(l4, l5))))
        flavors = set([Flavor.cherry, Flavor.banana,
                       Flavor.dirt, Flavor.earwax,
                       Flavor.cinnamon])
        self.assertEqual(tree.flavors(), flavors)

if __name__ == "__main__":
    unittest.main()


