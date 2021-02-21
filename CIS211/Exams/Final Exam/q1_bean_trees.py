"""Spring 2020 final exam problem:
every flavor beans
"""

from typing import List, Set
from enum import Enum, auto

class Flavor(Enum):
    banana = auto()
    black_pepper = auto()
    blueberry = auto()
    booger = auto()
    candyfloss = auto()
    cherry = auto()
    cinnamon = auto()
    dirt = auto()
    earthworm = auto()
    earwax = auto()


class Bertie_Bott_Bean_Tree:
    """Abstract base class"""

    def flavors(self) -> Set[Flavor]:
        """Returns the set of flavors growing in
        this tree.
        """
        raise NotImplementedError("Oops, no flavors method")

class Leaf(Bertie_Bott_Bean_Tree):
    """The beans are at the leaves"""
    def __init__(self, flavor: Flavor):
        self._bean = flavor

    def flavors(self) -> Set[Flavor]:
        return {self._bean}


class Branch(Bertie_Bott_Bean_Tree):
    """Inner node; the beans are not here"""
    def __init__(self,
                 left: Bertie_Bott_Bean_Tree,
                 right: Bertie_Bott_Bean_Tree):
        self._left = left
        self._right = right

    def flavors(self) -> Set[Flavor]:
        """Union of flavors on left and right"""
        return self._left.flavors().union(self._right.flavors())


# Hints:
#   The 'set' class is documented at
#   https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
#   You can make a singleton set like this: set([x])
#   You can take union like this:
#   m = set(['a', 'b'])
#   n = set(['b', 'c', 'd'])
#   u = m.union(n)
#   assert u == set(['a', 'b', 'c', 'd'])
#   assert u == set(['c', 'd', 'a', 'b'])
#   (note order is not significant)

