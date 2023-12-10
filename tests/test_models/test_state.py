#!/usr/bin/python3
"""
Testing the State class
"""

import unittest
from models.state import State


class StateTestCase(unittest.TestCase):
    """Unittest subclass"""

    def test_name(self):
        self.assertEqual(type(State.name), str, True)
