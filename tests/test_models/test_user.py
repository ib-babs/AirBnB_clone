#!/usr/bin/python3
"""
Testing the User class
"""

import unittest
from models.user import User


class UserTestCase(unittest.TestCase):
    """Unittest subclass"""

    def test_email(self):
        self.assertEqual(type(User.email), str, True)

    def test_password(self):
        self.assertEqual(type(User.password), str, True)

    def test_first_name(self):
        self.assertEqual(type(User.first_name), str, True)

    def test_last_name(self):
        self.assertEqual(type(User.last_name), str, True)
