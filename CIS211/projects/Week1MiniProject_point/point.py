import test_point


class Point:
    """A Point is a pair (x,y) denoting a point
        on the cartesion plane.  We use integer coordinates.
    """

    def __init__(self, x:int, y:int) -> None:
        """ initializes x and y onto self"""
        self.x = x
        self.y = y

    def move(self, dx: int, dy: int) -> None:
        """ increases self by dx and dy"""
        self.x = self.x + dx
        self.y = self.y + dy

    def __eq__(self, point2) -> bool:
        """checks if two points are equivalent"""
        if self.x == point2.x and self.y == point2.y:
            return True
        else:
            return False

    def __str__(self) -> str:
        """returns readable version of instance of class"""
        return f"({self.x}, {self.y})"