#!/usr/bin/python3
"""HBNBCommand class is an entry point of the command interpreter"""
import cmd
import re
import helps
import shlex
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """
    class_models = {"BaseModel": BaseModel, "User": User, "Place": Place,
                    "State": State, "City": City,
                    "Amenity": Amenity, "Review": Review}

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
