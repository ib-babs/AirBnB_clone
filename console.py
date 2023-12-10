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
import validators as vl


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in shlex.split(arg)]
        else:
            lexer = shlex.split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = shlex.split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


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
        print("")
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        args = arg.split()
        if not vl.validate_class(self, args):
            return
        new_model = self.class_models[args[0]]()
        new_model.save()
        print(new_model.id)

    def help_create(self):
        helps.create_help()

    def do_show(self, arg):
        args = arg.split()

        instance = storage.all()
        if not vl.validate_class(self, args, True, instance):
            return
        key = "{}.{}".format(args[0], args[1])
        print(instance[key])

    def help_show(self):
        helps.show_help()

    def do_destroy(self, arg):
        args = arg.split()
        instance = storage.all()
        if not vl.validate_class(self, args, True, instance):
            return
        key = "{}.{}".format(args[0], args[1])
        del instance[key]
        storage.save()

    def help_destroy(self):
        helps.destroy_help()

    def do_all(self, arg):
        args = arg.split()
        instance = storage.all()
        if len(args) > 0:
            if args[0] not in self.class_models.keys():
                print("** class doesn't exist **")
            else:
                initial_key = args[0]
                vl.validate_cmd(self, instance, chk_lst=True,
                                key=initial_key, string_list=True)

        elif len(args) == 0:
            print([str(val) for val in instance.values()])

    def help_all(self):
        helps.all_help()

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.class_models:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def default(self, arg: str) -> None:
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def help_update(self):
        helps.update_help()

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
