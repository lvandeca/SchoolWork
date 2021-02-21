"""CIS 211 Final Exam problem.
We always wear our masks.
"""
from typing import Tuple
# Colors are sometimes encoded in a format called
# RGBA, for "Red, Green, Blue, Alpha".
# The first three components (RGB) represent a color,
# as levels 0..255 of a primary color.  The fourth
# component (A) represents transparency, which we can
# also represent as an integer between 0 for transparent
# to 255 for entirely opaque.
#
# The r component is

def rgba_pack(r: int, g: int, b: int, alpha: int) -> int:
    """Pack red, green, blue, alpha into 32 bits"""
    assert 0 <= r <= 255
    assert 0 <= g <= 255
    assert 0 <= b <= 255
    assert 0 <= alpha <= 255

    packed = (r << 8) | g
    packed = (packed << 8) | b
    packed = (packed << 8) | alpha
    return packed


def rgba_unpack(rgba: int) -> Tuple[int, int, int, int]:
    """Unpack rgba into r, g, b, alpha"""
    alpha = rgba & 255
    b = (rgba >> 8) & 255
    g = (rgba >> 16) & 255
    r = (rgba >> 24)
    return (r, g, b, alpha)

def main():
    """Smoke test (also included in test_rgba.py)"""
    assert rgba_pack(0xAF, 0xBF, 0xCF, 0xF8) == 0xAFBFCFF8
    assert rgba_unpack(0x11223344) == (0x11, 0x22, 0x33, 0x44)

if __name__ == "__main__":
    main()


