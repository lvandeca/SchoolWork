"""Unit tests for Powerpuff Girls Residual Distribution.
All must be paid fairly!
"""
import unittest
from q3_powerpuff import *

class Test_1_Powerpuff(unittest.TestCase):

    def test_0_simple(self):
        """Our heroes"""
        buttercup = Character("Buttercup")
        blossoms = Character("Blossoms")
        bubbles = Character("Bubbles")
        professor = Character("Professor Utonium")
        buttercup.credit("All episodes", 3000.0)
        blossoms.credit("All episodes", 3000.0)
        bubbles.credit("All episodes", 3000.0)
        professor.credit("Several episodes", 1000.0)
        cast = Cast([buttercup, blossoms, bubbles, professor])
        cast.payout(10000.0)
        self.assertAlmostEqual(professor.assets(), 1000.0)
        self.assertAlmostEqual(buttercup.assets(), 3000.0)
        self.assertAlmostEqual(blossoms.assets(), 3000.0)
        self.assertAlmostEqual(bubbles.assets(), 3000.0)

    def test_1_villains(self):
        """The same as the example in q3_powerpuff.py"""
        mojo = Villain("Mojo Jojo", evil=10.0, clever=11.0)
        fuzzy = Villain("Fuzzy Lumpkins", evil=7.5, clever=1.7)
        princess = Villain("Princess Morbucks", evil=8.5, clever=5.2)
        him = Villain("HIM", evil=10.0, clever=8.7)

        cast = Cast([mojo, fuzzy, princess, him])

        mojo.credit("Monkey see, doggy doo", 20.0)
        mojo.credit("The Beat-alls", 5.0)
        fuzzy.credit("Meat Fuzzy Lumpkins", 10.0)
        him.credit("Octi evil", 20.0)
        fuzzy.credit("Fuzzy logic", 10.0)
        mojo.credit("Mr Mojo Rising", 15.0)
        princess.credit("Stuck up, up and away", 10.0)
        mojo.credit("Child Fearing", 10.0)
        # Conveniently sums to 100 minutes of on-screen time
        # Mojo: 50, Fuzzy: 20, Princess: 10, HIM: 20

        cast.payout(1000.00)  # Split the cash!
        self.assertAlmostEqual(mojo.assets(), 500.00)
        self.assertAlmostEqual(fuzzy.assets(), 200.0)
        self.assertAlmostEqual(princess.assets(), 100.0)
        self.assertAlmostEqual(him.assets(), 200.0)

if __name__ == "__main__":
    unittest.main()