#!/usr/bin/env python3
import cmd
from datetime import datetime
import json
from pprint import pprint

from mongoengine.errors import DoesNotExist, FieldDoesNotExist, ValidationError
from models.User import User
from models.Client import Client
from models.Tickets import Tickets
from models.StatusUpdate import StatusUpdates
from models import mongo_setup
from mongoengine import *
import shlex

classes = {"User": User, "Client": Client,
           "Tickets": Tickets, "StatusUpdates": StatusUpdates}

def save(obj):
    """ saves the obj while updating the time """
    obj.updated_at = datetime.utcnow()
    obj.save()

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
            try:
                instance = classes[args[0]].from_json(args[1])
                
            except FieldDoesNotExist:           #protects from wrong fields in the json
                print("Mr. T doesn't know one of those fields, fool")
                return False
            
        else:
            print("** class doesn't exist **")
            return False
        try:
            instance.save()
        except ValidationError:
            print("Required field is missing")

    def quickpop(self, a_dict):
        """ Pops uneeded keys"""
        a_dict.pop('created_at', None)
        a_dict.pop('updated_at', None)
        a_dict.pop('status_updates', None)
        return a_dict

    

    def status_updates(self, original, up_dict):
        """ creates the status update doc to be embbeded """
        og_dict = json.loads(original.to_json())
        self.quickpop(og_dict)
        self.quickpop(up_dict)
        og_keys = og_dict.keys()
        up_keys = up_dict.keys()
         
        
        if len(og_dict) < len(up_keys):
            key_diff1 = up_keys - og_keys
        elif len(og_dict) > len(up_keys):
            key_diff = og_keys - up_keys
        
        if key_diff:
            descrip = "Removed following info: {}".format(key_diff)
        elif key_diff1:
            descrip = "Added following info: {}".format(key_diff1)

        up_dict.pop('_id', None)
        for key, val in up_dict.items():
            descrip = descrip + "\n Changed {} : {}".format(key ,val)
        stat = {}
        stat['created_by'] = User.objects.get(id='616475474fa035538531b08b') 
        stat['description'] = descrip
        original.status = up_dict['status']
        original.status_updates.append(StatusUpdates(**stat))
        original.save()

        
        

    def do_update(self, arg):
        """ Updates given obj """
        args = arg.split(' ', 1)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            instance = json.loads(args[1])
            og_id = json.loads(args[1])
            og_id = og_id['_id']['$oid']
            original = Tickets.objects.get(id=og_id)
        else:
            print("** class doesn't exist **")
            return False
        self.status_updates(original, instance)

    def do_show(self, arg):
        """ looks for the specified obj by given id """
        args = arg.split(' ', 1)
        if len(args) == 0:
            print("Missing class name fool")
            return False
        if len(args) == 1:
            print("Missing ID, fool")
            return False
        if args[0] in classes:
            try:
                instance = classes[args[0]].objects.get(id=args[1])
                pprint(instance.to_json())
            except DoesNotExist:
                print("I pity the fool who don't know his ticket id")
        else:
            print("Mr. T pity the fool who doesn't know the classes")
            return False

    
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
