#!/usr/bin/python3
"""
Testing the console
"""

from io import StringIO
import helps
import unittest
from unittest.mock import patch
from console import HBNBCommand as HB
from models.base_model import BaseModel


class ConsoleTestCase(unittest.TestCase):
    """Unittest subclass"""

    def test_EOF(self):
        self.assertTrue(HB.do_EOF, True)

    def test_EOF_help(self):
        EOF = output_interception("help EOF")
        assert_msg(self, "EOF signal to exit the program.", EOF)

    def test_quit(self):
        self.assertTrue(HB.do_quit, True)

    def test_quit_help(self):
        quit = output_interception("help quit")
        assert_msg(self, "Quit command to exit the program.", quit)

    def test_emptyLine(self):
        self.assertIsNone(HB.emptyline(self), None)

    def test_all(self):
        all = output_interception("all Places")
        assert_msg(self, "** class doesn't exist **", all)

    def test_all_help(self):
        all = output_interception("help all")
        assert_msg(self, helps.all, all)

    def test_create(self):
        validate_class(self, "create", "create BaseM")

    def test_create_help(self):
        create = output_interception("help create")
        assert_msg(self, helps.create, create)

    def test_show(self):
        validate_class(self, "show", "show Us")

    def test_show_help(self):
        show = output_interception("help show")
        assert_msg(self, helps.show, show)

    def test_destroy(self):
        validate_class(self, "destroy", "destroy Us")
        instance_missing = output_interception("destroy User")
        assert_msg(self, "** instance id missing **", instance_missing)
        non_instance = output_interception("destroy User 01923-")
        assert_msg(self, "** no instance found **", non_instance)

    def test_destroy_help(self):
        destroy = output_interception("help destroy")
        assert_msg(self, helps.destroy, destroy)

    def test_update(self):
        validate_class(self, "update", "update Me")
        instance_missing = output_interception("update User")
        assert_msg(self, "** instance id missing **", instance_missing)
        non_instance = output_interception("update User 01923-")
        assert_msg(self, "** no instance found **", non_instance)

    def test_update_help(self):
        update = output_interception("help update")
        assert_msg(
            self, helps.update, update)

    def test_class_show(self):
        validate_cmd(self, "Use.show()", "User.show()", "User.show(10)")

    def test_class_update(self):
        validate_cmd(self, "Use.update()", "User.update()",
                     'User.update(10, )')


def output_interception(method=""):
    with patch('sys.stdout', new=StringIO()) as f:
        new_instance = HB()
        new_instance.onecmd(method)
        printed = f.getvalue().strip()
    return printed


def validate_class(self, cls_name1, cls_name2):
    mising_class_name = output_interception(cls_name1)
    self.assertIn("** class name missing **", mising_class_name)
    non_exist_class = output_interception(cls_name2)
    self.assertIn("** class doesn't exist **", non_exist_class)


def assert_msg(self, msg, method):
    output_interception(method)
    self.assertIn(msg, method)


def validate_cmd(self, cls1, cls2, cls3):
    non_exist_class = output_interception(cls1)
    self.assertIn("** class doesn't exist **", non_exist_class)
    missing_instance = output_interception(cls2)
    self.assertIn("** instance id missing **", missing_instance)
    non_instance = output_interception(cls3)
    self.assertIn("** no instance found **", non_instance)
