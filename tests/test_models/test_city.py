#!/usr/bin/python3
"""
Testing the City class
"""

import unittest
from models.city import City


class CityTestCase(unittest.TestCase):
    """Unittest subclass"""

    def test_state_id(self):
        self.assertEqual(type(City.state_id), str, True)

    def test_name(self):
        self.assertEqual(type(City.name), str, True)
