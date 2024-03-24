#!/usr/bin/python3
"""
    A module that contains the HBNBCommand class
"""
import re
import sys
import cmd
import json
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {"BaseModel": BaseModel, "User": User, "City": City,
            "State": State, "Amenity": Amenity, "Review": Review,
            "Place": Place
            }


class HBNBCommand(cmd.Cmd):
    """
        The class of the command interpreter
    """
    prompt = f"(hbnb) " if sys.__stdin__.isatty() else ''

    def preloop(self):
        """
            Checks if the interpreter is in interactive mode
        """
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    # PRE CMD
    def precmd(self, line):
        """
            Parses the command line's input
        """
        # Check for .()
        if not ("." in line and "(" in line and ")" in line):
            return line

        _cls = line.split('.')[0]
        if _cls not in classes.keys():
            print("** class doesn't exist **")
            return line
        if _cls:
            args = re.findall(rf'{_cls}\.([a-zA-Z_]+)\((.*?)\)', line)
            if args:
                cmd = list(args[0])
                # print(f"cmd: {cmd[1]}")
                if cmd[0] == "update":
                    paras = cmd[1].split(',')
                    paras = [item.strip() for item in paras]
                    print(f"PRECMD : {paras}")
                    line = f"{cmd[0]} {_cls} {paras[0]} {paras[1]} {paras[2]}"
                    return line
                cmd[1] = cmd[1].replace('"', '')
                line = f"{cmd[0]} {_cls} {cmd[1]}"
        return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, line):
        """Exits the program"""
        exit(0)

    def do_EOF(self, line):
        """Exits the program"""
        return True

    def emptyline(self):
        """Does nothing if emptyline is entered"""
        return ''

    def do_create(self, line):
        """Creates a new instance of BaseModel and saves it to JSON"""
        # classes = ['BaseModel']
        args = cmd.Cmd.parseline(self, line)
        if args[0] is None:
            print("** class name missing **")
        elif args[0] and args[0] not in classes:
            print("** class doesn't exist **")
        else:
            # new_inst = BaseModel()
            new_inst = classes[args[0]]()
            storage.new(new_inst)
            storage.save()
            print(new_inst.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        args = cmd.Cmd.parseline(self, line)
        if args[0] is None:
            print("** class name missing **")
        elif args[0] and args[0] not in classes:
            print("** class doesn't exist **")
        elif args[0] in classes and args[1] == '':
            print("** instance id missing **")
        else:
            try:
                with open("file.json", 'r', encoding="utf-8") as f:
                    data = json.load(f)
                key = f'{args[0]}.{args[1]}'
                if key not in data:
                    print("** no instance found **")
                else:
                    instance = classes[args[0]](**data[key])
                    print(instance)
            except FileNotFoundError:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance"""
        # classes = ['BaseModel']
        args = cmd.Cmd.parseline(self, line)
        if args[0] is None:
            print("** class name missing **")
        elif args[0] and args[0] not in classes:
            print("** class doesn't exist **")
        elif args[0] in classes and args[1] == '':
            print("** instance id missing **")
        else:
            try:
                with open("file.json", 'r', encoding="utf-8") as f:
                    data = json.load(f)
                key = f'{args[0]}.{args[1]}'
                if key not in data:
                    print("** no instance found **")
                else:
                    data.pop(key)
                    with open("file.json", 'w', encoding="utf-8") as f:
                        json.dump(data, f)
            except FileNotFoundError:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances"""
        all_instances = []
        args = cmd.Cmd.parseline(self, line)
        try:
            with open('file.json', 'r', encoding="utf-8") as f:
                data = json.load(f)
            if args[0] and args[0] not in classes:
                print("** class doesn't exist **")
            elif args[0] and args[0] in classes:
                for key in data.keys():
                    if args[0] in key:
                        instance = classes[args[0]](**data[key]).__str__()
                        all_instances.append(instance)
                print(all_instances)
            else:
                for key in data.keys():
                    name = data[key]['__class__']
                    instance = classes[name](**data[key]).__str__()
                    all_instances.append(instance)
                print(all_instances)
        except FileNotFoundError:
            pass

    # TO REDO
    def do_update(self, line):
        """ update <class name> <id> <attribute> <value>
            updates an attribute in a specific classname by a given value
        """
        # print(line)
        if not line:
            print(self.class_missing)
            return

        parsed_line = re.match(
            r'^(\S*)\s?(\S*)\s?("[^"]+"|\S*)?\s?("[^"]+"|\S*)', line)
        args = list(parsed_line.groups())
        all_inst = storage.all()
        # data_type = int

        if not self.class_check(args):
            return
        if not self.id_check(args, all_inst):
            return
        if not self.attribute_check(args):
            return

        key, value = args[2], args[3]
        try:
            value = eval(value)
        except Exception:
            pass

        search_key = f"{args[0]}.{args[1]}"
        wanted_inst = all_inst[search_key]
        setattr(wanted_inst, key, value)
        wanted_inst.save()

    class_missing = "** class name missing **"
    class_nexist = "** class doesn't exist **"
    id_missing = "** instance id missing **"
    inst_missing = "** no instance found **"
    attr_name_missing = "** attribute name missing **"
    attr_value_missing = "** value missing **"

    # HELPERS OF UPDATE
    def class_check(self, args):
        """checks the <classname> and handles it's errors"""
        if len(args) == 0 or not args[0]:
            print(self.class_missing)
            return False

        class_name = args[0]
        if class_name not in classes.keys():
            print(self.class_nexist)
            return False

        return True

    def id_check(self, args, instances):
        """checks the <id> and handles it's errors"""
        if len(args) == 1 or not args[1]:
            print(self.id_missing)
            return False

        args[1] = args[1].strip('"')
        key = f"{args[0]}.{args[1]}"
        if key not in instances.keys():
            print(self.inst_missing)
            return False

        return True

    def attribute_check(self, args):
        """checks the <attributes> and handles it's errors"""

        if len(args) == 2 or not args[2]:
            print(self.attr_name_missing)
            return False

        args[2] = args[2].strip('"')
        if args[2] in ['created_at', 'updated_at', 'id']:
            return False

        if not args[3]:
            print(self.attr_value_missing)
            return False

        return True

    def do_count(self, line):
        """ Counts the number of instances """
        args = cmd.Cmd.parseline(self, line)
        if args[0] is None:
            print("** class name missing **")
        elif args[0] and args[0] not in classes:
            print("** class doesn't exist **")
        else:
            with open("file.json", 'r', encoding="utf-8") as f:
                data = json.load(f)
                i = 0
                for key in data.keys():
                    if args[0] in key:
                        i += 1
            print(i)


if __name__ == "__main__":
    HBNBCommand().cmdloop()