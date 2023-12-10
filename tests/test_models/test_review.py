#!/usr/bin/python3
"""
Testing the Review class
"""

import unittest
from models.review import Review


class ReviewTestCase(unittest.TestCase):
    """Unittest subclass"""

    def test_place_id(self):
        self.assertEqual(type(Review.place_id), str, True)

    def test_user_id(self):
        self.assertEqual(type(Review.user_id), str, True)

    def test_text(self):
        self.assertEqual(type(Review.text), str, True)
