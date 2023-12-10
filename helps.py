#!/usr/bin/python3
"""
Help module
"""
create = "`create` method creates new instance based on classname`"

show = "`show` method display instance based on `id` and `classname`."

destroy = "`destroy` method destroy instance of classname"

all = "`all` method display instances based on `classname`"

update1 = """update <class name> <id>
 <attribute name> "<attribute value>\""""

update2 = """Usage: <class name>.update(<id>, 
<dictionary representation>"""


def create_help():
    print(create)


def show_help():
    print(show)


def destroy_help():
    print(destroy)


def all_help():
    print(all)


def update_help():
    print(update1)
