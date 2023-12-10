#!/usr/bin/python3
"""
Testing the filestorage
"""

import unittest
from models.engine.file_storage import FileStorage as FS
from models import storage


class FileStorageTestCase(unittest.TestCase):
    """Unittest subclass"""

    def test_all(self):
        self.assertTrue(hasattr(FS, "all"), True)

    def test_new(self):
        self.assertTrue(hasattr(FS, "new"), True)

    def test_save(self):
        self.assertTrue(hasattr(FS, "save"), True)

    def test_reload(self):
        self.assertTrue(hasattr(FS, "reload"), True)

    def test_isinstance(self):
        self.assertTrue(isinstance(storage, FS), True)
