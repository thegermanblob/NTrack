#!/usr/bin/env python3
import cmd
from pprint import pprint
from models.User import User
from models.Client import Client
from models.Tickets import Tickets
from models.StatusUpdate import StatusUpdates
from models import mongo_setup
from mongoengine import *
import shlex
classes = {"User": User, "Client": Client,
           "Tickets": Tickets, "StatusUpdates": StatusUpdates}


class NtrackCommand(cmd.Cmd):
    """ A console to test and develop the NTrack application """
    prompt = '(NTrack)'

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True


    def do_create(self, arg):
        """
            Creates a new instance of a class from a given json 
        """
        args = arg.split(' ', 1)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            instance = classes[args[0]].from_json(args[1])
        else:
            print("** class doesn't exist **")
            return False
        instance.save()
    
    def all_objs(self):
        """ prints all objs in db """
        for key in classes.keys():
            try:
                for obj in classes[key].objects.all():
                    pprint(obj.to_json())
                    print("")
            except:
                continue

    def do_all(self, arg):
        """ Gets all instances of a class """
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            self.all_objs()
        elif args[0] in classes:
            try:
                for obj in classes[args[0]].objects.all():
                    pprint(obj.to_json())
                    print("")
            except:
                pass
        else:
            print("** class doesn't exist **")
            return False

    

if __name__ == '__main__':
    mongo_setup.global_init()
    NtrackCommand().cmdloop()
