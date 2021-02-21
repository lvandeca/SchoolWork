"""Rows of tiles (Midterm problem)"""

import enum
from typing import List

class Color(enum.Enum):
    red = 1
    blue = 2

    def __str__(self) -> str:
        """'r' for red, 'b' for blue"""
        return self.name[0]

ABBREVIATIONS = { 'r': Color.red,
                  'b': Color.blue
                }


class Tile:
    """A single colored tile, either red or blue"""
    def __init__(self, tile_color: Color):
        self._color = tile_color

    def color(self) -> Color:
        return self._color

    def __eq__(self, other: "Tile"):
        """Tiles are equal if they have the same color"""
        return self._color == other._color

    def __str__(self) -> str:
        return str(self._color)


class Row:
    """A row of colored tiles"""
    def __init__(self):
        self.tiles = []

    def append(self, tile: Tile):
        "appends another Tile to Row"
        self.tiles.append(tile)

    def __str__(self) -> str:
        # for an empty Row
        return_string = ''
        # iterate through self.tiles
        for tile in self.tiles:
            # update return_string with the string of the tile
            return_string += tile.__str__()
        return return_string

    def __eq__(self, other: "Row") -> bool:
        return self.tiles == other.tiles

    def from_abbreviation(self, abbrv: str):
        # override any previous additions to self.tiles as stated in test cases line 41
        self.tiles = []
        # iterate through string of abbreviated colors
        for letter in abbrv:
            # update self.tiles with appropriate tile and color according to letter
            if letter == "r":
                self.tiles.append(Tile(Color.red))
            else:
                self.tiles.append(Tile(Color.blue))

def main():
    row = Row()
    row.append(Tile(Color.blue))
    row.append(Tile(Color.red))
    row.append(Tile(Color.blue))

    print(row)

    row2 = Row()
    row2.from_abbreviation("brb")
    assert row == row2

if __name__ == "__main__":
    main()
