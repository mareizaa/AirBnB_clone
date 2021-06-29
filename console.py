#!/usr/bin/python3
"""
program to console.py
"""
import cmd
from models import base_model
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    class console
    """
    prompt = "(hbnb) "

    def do_EOF(self, *args):
        """Command to exit the program
        """
        return True

    def do_quit(self, *args):
        """Quit command to exit the program
        """
        return True

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the json file)
        and prints the id
        """
        lista = args.split(" ")

        if lista[0] == "BaseModel":
            obj = BaseModel()
            print("{}".format(obj.id))
        elif lista[0] != "BaseModel":
            print("** class doesn´t exist **")
        else:
            print("** class name missing **")

    def do_show(self, args):
        """print the string representation of an instance
        based on the class name and id
        """
        lista = args.split(" ")
        res = storage.all()
        if lista[0] is "":
            print("** class name missing **")
        elif lista[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(lista) == 1:
            print("** instance id missing **")
        else:
            key = "BaseModel.{}".format(lista[1])
            if key not in res:
                print("** no instance found **")
            else:
                for value in res.values():
                    print(value)

if __name__ == '__main__':
    HBNBCommand().cmdloop()