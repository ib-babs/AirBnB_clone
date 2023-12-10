#!/usr/bin/python3
"""
Testing the Place class
"""

import unittest
from models.place import Place


class UserTestCase(unittest.TestCase):
    """Unittest subclass"""

    def test_user_id(self):
        self.assertEqual(type(Place.user_id), str, True)

    def test_city_id(self):
        self.assertEqual(type(Place.city_id), str, True)

    def test_name(self):
        self.assertEqual(type(Place.name), str, True)

    def test_description(self):
        self.assertEqual(type(Place.description), str, True)

    def test_number_rooms(self):
        self.assertEqual(type(Place.number_rooms), int, True)

    def test_number_bathrooms(self):
        self.assertEqual(type(Place.number_bathrooms), int, True)

    def test_max_guest(self):
        self.assertEqual(type(Place.max_guest), int, True)

    def test_price_by_night(self):
        self.assertEqual(type(Place.price_by_night), int, True)

    def test_amenity_ids(self):
        self.assertEqual(type(Place.amenity_ids), list, True)
