#!/usr/bin/python3
"""
FileStorage class is a that
serializes instances to a JSON file and deserializes JSON file to instances:
"""
import json
import os

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """FileStorage definition"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns object dictionary"""
        return self.__objects

    def new(self, obj):
        """Set id"""
        if obj:
            baseId = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[baseId] = obj

    def save(self):
        """Serializing __object"""
        with open(self.__file_path, "w", encoding="UTF-8") as fp:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, fp)

    def reload(self):
        """Deserializing file json"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="UTF-8") as fp:
                new_dict = {}
                read_it = fp.read()
                if len(read_it) > 0 and read_it != "{}":
                    new_dict = json.loads(read_it)
            if new_dict is not None and len(new_dict) > 0:
                for value in new_dict.values():
                    # # Approach
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
                    # Approach 2
                    # cls = globals()[value["__class__"]]
                    # cls(**value)
