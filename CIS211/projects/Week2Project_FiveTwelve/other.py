def to_list(self) -> List[List[int]]:
    """Test scaffolding: represent each Tile by its
    integer value and empty positions as 0
    """
    result = []
    for row in self.tiles:
        row_values = []
        for col in row:
            if col is None:
                row_values.append(0)
            else:
                row_values.append(col)  # changed this from col.value to col -> check later if problems
        result.append(row_values)
    return result


def from_list(self, values: List[List[int]]):
    """Test scaffolding: set board tiles to the
    given values, where 0 represents an empty space.
    """
    self.tiles = []
    for row in values:
        row_values = []
        for col in row:
            if col is 0:
                row_values.append(None)
            else:
                row_values.append(col)
        self.tiles.append(row_values)
    return self.tiles


def in_bounds(self, pos: Vec) -> bool:
    """Is position (pos.x, pos.y) a legal position on the board?"""
    return (0 <= pos.y < self.cols) and (0 <= pos.x < self.rows)


def slide(self, pos: Vec, dir: Vec):
    """Slide tile at row,col (if any)
    in direction (dx,dy) until it bumps into
    another tile or the edge of the board.
    """
    if self[pos] is None:
        return
    while True:
        new_pos = pos + dir
        if not self.in_bounds(new_pos):
            break
        if self[new_pos] is None:
            self._move_tile(pos, new_pos)
        elif self[pos] == self[new_pos]:
            self[pos].merge(self[new_pos])
            self._move_tile(pos, new_pos)
            break  # Stop moving when we merge with another tile
        else:
            # Stuck against another tile
            break
        pos = new_pos


def _move_tile(self, old_pos: Vec, new_pos: Vec):
    old_pos_value = self[old_pos]
    self.tiles[old_pos.x][old_pos.y] = None
    self.tiles[new_pos.x][new_pos.y] = old_pos_value









