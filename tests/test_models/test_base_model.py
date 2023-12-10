#!/usr/bin/python3
"""
Testing the BaseModel
"""

import unittest
from models.base_model import BaseModel as BS
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class BaseModelTestCase(unittest.TestCase):
    """Unittest subclass"""

    def test_user(self):
        user = User()
        self.assertTrue(isinstance(user, User), True)

    def test_userbaseclass(self):
        self.assertEqual(User.__base__.__name__, "BaseModel", True)

    def test_base_model(self):
        bs = BS()
        self.assertTrue(isinstance(bs, BS), True)

    def test_place(self):
        place = Place()
        self.assertTrue(isinstance(place, Place), True)

    def test_place_baseclass(self):
        self.assertEqual(Place.__base__.__name__, "BaseModel", True)

    def test_state(self):
        state = State()
        self.assertTrue(isinstance(state, State), True)

    def test_state_baseclass(self):
        self.assertEqual(State.__base__.__name__, "BaseModel", True)

    def test_city(self):
        city = City()
        self.assertTrue(isinstance(city, City), True)

    def test_city_baseclass(self):
        self.assertEqual(City.__base__.__name__, "BaseModel", True)

    def test_amenity(self):
        amenity = Amenity()
        self.assertTrue(isinstance(amenity, Amenity), True)

    def test_amenity_baseclass(self):
        self.assertEqual(Amenity.__base__.__name__, "BaseModel", True)

    def test_review(self):
        review = Review()
        self.assertTrue(isinstance(review, Review), True)

    def test_review_baseclass(self):
        self.assertEqual(Review.__base__.__name__, "BaseModel", True)
