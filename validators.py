#!/usr/bin/python3
"""Validators"""
import re


def validate_class(self, args, check_id=False, instance={}):
    if len(args) < 1:
        print("** class name missing **")
        return False
    if args[0] not in self.class_models.keys():
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


def validate_cmd(self, inst={}, chk_lst=False,
                 cnt=False, key="", string_list=False):
    count = 0
    append_cls_list = []
    if self.class_models.get(key):
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
