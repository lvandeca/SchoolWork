"""IntervalCollection (midterm problem, CIS 211)"""

from typing import List

class Interval:
    """A closed interval of integers contains its end points"""
    def __init__(self, bound_low: int, bound_high: int):
        self.low = bound_low
        self.high = bound_high

    def __repr__(self) -> str:
        return f"Interval({self.low}, {self.high})"

    def __str__(self) -> str:
        return f"[{self.low}, {self.high}]"

    def contains(self, i: int) -> bool:
        # checks if value i between upper and lower bounds of Interval
        return self.low <= i <= self.high


class IntervalCollection:
    """Wraps a list of closed intervals"""
    def __init__(self):
        self.items: List[Interval]  = [ ]

    def append(self, interval: Interval):
        """Add interval to the list of intervals"""
        # appends item to a list of type IntervalCollection
        self.items.append(interval)

    def contains(self, i: int) -> bool:
        """True if any interval contains i"""
        # iterates through list of Intervals
        for interval in self.items:
        # checks if interval contains element i
            if interval.contains(i):
                return True
        # if entire list has been iterated through and no intervals contains i, then return False
        return False


