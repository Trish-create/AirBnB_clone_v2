#!/usr/bin/python3

import cmd
import shlex

from models import storage
from models.base_model import BaseModel
from models.state import State
from models.place import Place
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB project."""

    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel,
        "State": State,
        "City": City,
        "Place": Place,
        "User": User,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_quit(self, arg):
        """Quit the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Handle EOF."""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, arg):
        """Create a new instance with optional parameters."""
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[class_name]()

        for parameter in args[1:]:
            if "=" not in parameter:
                continue

            key, value = parameter.split("=", 1)

            if not key or not value:
                continue

            if value.replace(".", "", 1).replace("-", "", 1).isdigit():
                if "." in value:
                    value = float(value)
                else:
                    value = int(value)
            else:
                value = value.replace("_", " ")

            setattr(new_instance, key, value)

        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """This will print the string representation."""
        if not arg:
            print("** class name is missing **")
            return

        args = arg.split()

        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]

        objects = storage.all()

        key = "{}.{}".format(class_name, instance_id)

        if key not in objects:
            print("** no instance found **")
            return

        print(objects[key])

    def do_all(self, arg):
        """Print all instances or all instances of a class."""
        objects = storage.all()

        if not arg:
            print([str(obj) for obj in objects.values()])
            return

        class_name = arg.strip()

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        print([
            str(obj)
            for obj in objects.values()
            if obj.__class__.__name__ == class_name
        ])


if __name__ == "__main__":
    storage.reload()
    HBNBCommand().cmdloop()
