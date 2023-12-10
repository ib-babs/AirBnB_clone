#!/usr/bin/python3
"""Console Module
HBNBCommand class is an entry point of the command interpreter
This module controls all databases
"""
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


class_models = {"BaseModel": BaseModel, "User": User, "Place": Place,
                "State": State, "City": City,
                "Amenity": Amenity, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """Cmd subclass"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """"Quit command to exit the program\n"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        args = arg.split()
        if not validate_class(args):
            return
        new_model = class_models[args[0]]()
        new_model.save()
        print(new_model.id)

    def help_create(self):
        helps.create_help()

    def do_show(self, arg):
        args = arg.split()

        instance = storage.all()
        if not validate_class(args, True, instance):
            return
        key = "{}.{}".format(args[0], args[1])
        print(instance[key])

    def help_show(self):
        helps.show_help()

    def do_destroy(self, arg):
        args = arg.split()
        instance = storage.all()
        if not validate_class(args, True, instance):
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
            if args[0] not in class_models.keys():
                print("** class doesn't exist **")
            else:
                initial_key = args[0]
                validate_cmd(instance, chk_lst=True,
                             key=initial_key, string_list=True)

        elif len(args) == 0:
            print([str(val) for val in instance.values()])

    def help_all(self):
        helps.all_help()

    def do_update(self, arg):
        args = shlex.split(arg)
        instance = storage.all()
        if not validate_class(args, True, instance):
            return
        if not validate_attr(args):
            return
        CONSTANTS = ["id", "updated_at", "created_at"]
        key = "{}.{}".format(args[0], args[1])

        if not args[2] in CONSTANTS:
            if not instance.get(args[2]):
                instance[key].__dict__[args[2]] = args[3]
            elif instance.get(args[2]):
                if isinstance(instance.get(args[2]), (str, int, float)):
                    instance[key].__dict__[args[2]] = args[3]
            instance[key].save()

    def default(self, line: str) -> None:
        instance = storage.all()
        reuse_class = re.compile(r".*\.")
        reuse_id = re.compile(r'(?<=["\(]).*[^"\)]')
        initial_cmd = line.split()[0]
        initial_key = reuse_class.match(initial_cmd)
        method = re.search(r"(?<=\.).*\(",  line)

        if initial_key and method:
            initial_key = initial_key.group().replace(".", "")
            method = method.group().replace("(", "")
            match(method):
                case "all":
                    validate_cmd(instance, chk_lst=True, key=initial_key)
                    return

                case "count":
                    validate_cmd(instance, cnt=True, key=initial_key)
                    return

                case "show":
                    re_key = reuse_id.search(line)
                    if not validate_class([initial_key, re_key]):
                        return
                    if not validate_id(re_key):
                        return
                    re_key = re_key.group().replace('"', "")
                    return self.do_show(initial_key+" "+re_key)

                case "destroy":
                    id = reuse_id.search(line)
                    if not validate_id(id):
                        return
                    id = id.group().replace('"', "")
                    return self.do_destroy(f"{initial_key} {id}")

                case "update":
                    id = re.search(r'(?<=["\(]).*[\{,\)].', line)
                    if not validate_class([initial_key, id]):
                        return
                    if not validate_id(id):
                        return
                    id = re.sub(r'[",\{\} \)]', "", id.group())

                    if not validate_class([initial_key, id[:36]],
                                          True, instance):
                        return
                    rip_dict = re.search(r"(?<=\{).*[^\}\)]", line)
                    if not rip_dict:
                        print(
                            """Usage: <class name>.update(<id>, \
<dictionary representation>""")
                        return
                    rip_dict = rip_dict.group()
                    parse = [re.sub(r'["\',]', "", i.strip(" "))
                             for i in re.split(r"[:,]", rip_dict)
                             if len(i) > 0]
                    try:
                        parse.remove("")
                    except Exception as e:
                        pass

                    if len(parse) % 2 == 0:
                        i = 0
                        while i < len(parse):
                            if i < len(parse) - 1:
                                args = f"""{initial_key} {id[:36]}
                                '{parse[i]}' '{parse[i+1]}'"""
                                self.do_update(args)
                                i += 2
                        return
                    elif len(parse) % 2 == 1:
                        args = [initial_key, id[:36], parse[0]]
                        if not validate_attr(args):
                            return

        return super().default(line)

    def help_update(self):
        helps.update_help()


def validate_class(args, check_id=False, instance={}):
    if len(args) < 1:
        print("** class name missing **")
        return False
    if args[0] not in class_models.keys():
        print("** class doesn't exist **")
        return False
    if len(args) < 2 and check_id:
        print("** instance id missing **")
        return False
    if len(instance) > 0 and len(args) > 1 and args[1] is not None:
        key = "{}.{}".format(args[0], args[1])
        if not instance.get(key):
            print("** no instance found **")
            return False
    return True


def validate_attr(args):
    if len(args) == 2:
        print("** attribute name missing **")
        return False
    elif len(args) == 3:
        print("** value missing **")
        return False

    return True


def validate_cmd(inst={}, chk_lst=False, cnt=False, key="", string_list=False):
    count = 0
    append_cls_list = []
    if class_models.get(key):
        for k in inst.keys():
            key_match = re.fullmatch(fr"{key}.*", k)
            if key_match is not None:
                key_match = key_match.group()
                if string_list:
                    append_cls_list.append(str(inst[key_match]))
                else:
                    append_cls_list.append(inst[key_match])
                count += 1
        if chk_lst:
            print(append_cls_list)
            return
        else:
            print(count)
            return


def validate_id(word):
    if word is None:
        print("** instance id missing **")
        return False
    return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
