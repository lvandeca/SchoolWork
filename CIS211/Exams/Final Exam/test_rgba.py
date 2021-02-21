"""Test cases for q2_rgba.py."""

import unittest
from q2_rgba import *

class Test_RGBA_Basic(unittest.TestCase):
    """Same as exaple in q2_rgba.py"""

    def test_example_pack(self):
        packed = rgba_pack(0xAF, 0xBF, 0xCF, 0xF8)
        self.assertEqual(packed, 0xAFBFCFF8)
        # Note 0x begins a hex number; each hex digit corresponds
        # to 4 binary digits

    def test_example_unpack(self):
        r, g, b, a = rgba_unpack(0x11223344)
        self.assertEqual(r, 0x11)
        self.assertEqual(g, 0x22)
        self.assertEqual(b, 0x33)
        self.assertEqual(a, 0x44)


class Test_RGBA_Extras(unittest.TestCase):
    """A few more, just for good measure"""

    def test_transparent(self):
        """Zeros in every channel"""
        transparent = rgba_pack(0, 0, 0, 0)
        self.assertEqual(transparent, 0x0)
        channels = rgba_unpack(transparent)
        self.assertEqual(channels, (0, 0, 0, 0))

    def test_opaque(self):
        """From HTML color picker in Google search"""
        opaque_marine = rgba_pack(50, 168, 164, 255)
        self.assertEqual(opaque_marine, 0x32a8a4ff)
        r, g, b, a = rgba_unpack(opaque_marine)
        self.assertEqual(r, 50)
        self.assertEqual(g, 168)
        self.assertEqual(b, 164)
        self.assertEqual(a, 255)

if __name__ == "__main__":
    unittest.main()

