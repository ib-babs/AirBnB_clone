#!/usr/bin/python3
"""
Testing the Amenity class
"""

import unittest
from models.amenity import Amenity


class AmenityTestCase(unittest.TestCase):
    """Unittest subclass"""

    def test_name(self):
        self.assertEqual(type(Amenity.name), str, True)
