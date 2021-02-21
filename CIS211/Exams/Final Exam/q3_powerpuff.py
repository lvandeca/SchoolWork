"""Powerpuff Girls residuals payments.
2020 Spring CIS 211 exam problem.
This might possibly involve a two-pass algorithm.
"""
from typing import List

class Character:
    """A character in PowerPuff Girls animated series"""
    def __init__(self, name: str):
        self._name = name
        self._money = 0.0
        self._screen_time = 0.0

    def pay(self, amt: float):
        """Even imaginary actors should be paid"""
        self._money += amt

    def assets(self) -> float:
        """Are we rich yet?"""
        return self._money

    def credit(self, title: str, minutes: float):
        """Credit for appearance in an episode"""
        self._screen_time += minutes

    def screen_time(self) -> float:
        return self._screen_time


class Villain(Character):
    def __init__(self, name: str, evil: float, clever: float):
        super().__init__(name)
        self.evil = evil
        self.clever = clever


class Cast:
    def __init__(self, characters: List[Character]):
        self.characters = characters

    def payout(self, amt: float):
        """Distribute the payout in proportion to total
        screen time.  If character X was on screen twice
        as much as character Y, they should be paid twice
        as much.  Total payment must be amt (within a few cents).
        """

        # first pass for total screen time
        total_time = 0
        for character in self.characters:
            total_time += character.screen_time()

        # second pass for weighted pay per character
        for character in self.characters:
            cash = amt * (character.screen_time() / total_time)
            character.pay(cash)

def main():
    # Example:
    # Buttercup, Blossom, and Bubbles are paid separately;
    # the villains are paid in proportion to screen time
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
    assert abs(mojo.assets() - 500.00) < 1.0
    assert abs(fuzzy.assets() - 200.0) < 1.0
    assert abs(princess.assets() - 100.0) < 1.0
    assert abs(him.assets() - 200.0) < 1.0

if __name__ == "__main__":
    main()
    print("Success")
















