from math import pi


class Shape3d:

    def volume(self) -> float:
        return NotImplementedError("Not implemented for abstract class")

    def area(self) -> float:
        return NotImplementedError("Not implemented for abstract class")

    def print_info(self) -> str:
        print(f"Area:{self.area()} Volume:{self.volume()}")


class Cylinder(Shape3d):

    def __init__(self, radius: float, height: float):
        self.radius = radius
        self.height = height

    def volume(self) -> float:
        return (self.radius**2) * self.height * pi

    def area(self) -> float:
        radius_sqr = self.radius ** 2
        return (2 * pi * radius_sqr) + (2 * pi * self.radius * self.height)


class Cuboid(Shape3d):

    def __init__(self, width: float, length: float, height: float):
        self.width = width
        self.length = length
        self.height = height

    def volume(self) -> float:
        return self.width * self.length * self.height

    def area(self) -> float:
        return (2 * self.width * self.length) + (2 * self.width * self.height) + (2 * self.length * self. height)


class Cube(Cuboid):

    def __init__(self, width: float):
        self.width = width
        self.length = width
        self.height = width


