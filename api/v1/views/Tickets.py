""" Module containing all RESTful api actions for Tickets """
from mongoengine.errors import DoesNotExist, FieldDoesNotExist, ValidationError
from api.v1.app import app_views
from flasgger import swag_from
from flask import json, jsonify, request, abort
from models.Client import Client
from models.Tickets import Tickets
from models.User import User
from models.StatusUpdate import StatusUpdates

@app_views.route('/tickets', methods=['GET'], strict_slashes=False)
@swag_from('apidoc/all_tickets.yml')
def all_tickets():
    """ Returns all tickets """ 
    return Tickets.objects.to_json()


@app_views.route('/tickets/<tstatus>', methods=['GET'], strict_slashes=False)
@swag_from('apidoc/ticketstatus.yml')
def ticket_status(tstatus):
    """ Returns tickets that match status """
    return Tickets.objects(status=tstatus).to_json()

@app_views.route('/tickets', methods=['POST'], strict_slashes=False)
@swag_from('apidoc/post_ticket.yml')
def post_ticket():
    """ Takes a ticket json and adds it to the Database """
    new = request.get_json()
    if not new:
        abort(404, description="Not a JSON")

    new = json.loads(new)
    new.pop('_id', None)
    new = Tickets(**new)
    new.save()
    return (new.to_json)

@app_views.route('/ticket/<ticket_id>', methods=['GET'], strict_slashes=False)
@swag_from('apidoc/get_ticket.yml')
def get_ticket(ticket_id):
    """ gets ticket if it is in the database """
    try:
        instance = Tickets.objects.get(id=ticket_id)
        return instance.to_json()
    except DoesNotExist:
        abort(404, description="Ticket_id does not exist")
    except ValidationError:
        abort(400, description="Invalid Id")



def quickpop(a_dict):
    """ Pops uneeded keys"""
    a_dict.pop('created_at', None)
    a_dict.pop('updated_at', None)
    a_dict.pop('status_updates', None)
    a_dict.pop('client_id', None)
    return a_dict



def st_updates(original, up_dict):
    """ creates the status update doc to be embbeded """
    og_dict = json.loads(original.to_json())
    quickpop(og_dict)
    quickpop(up_dict)
    og_keys = og_dict.keys()
    up_keys = up_dict.keys()
        
    # Verify what atributes we are adding or removing
    if len(og_dict) < len(up_keys):
        key_diff1 = up_keys - og_keys
    elif len(og_dict) > len(up_keys):
        key_diff = og_keys - up_keys
    
    if key_diff:
        descrip = "Removed following info: {}".format(key_diff)
    elif key_diff1:
        descrip = "Added following info: {}".format(key_diff1)

    #prepares description for status update
    up_dict.pop('_id', None)
    for key, val in up_dict.items():
        descrip = descrip + "\n Changed {} : {}".format(key ,val)
    stat = {}
    stat['created_by'] = User.objects.get(id='616475474fa035538531b08b') #todo change user to session user 
    stat['description'] = descrip
    original.status = up_dict['status']

    original.status_updates.append(StatusUpdates(**stat))
    original.save()  


@app_views.route('/tickets/<ticket_id>', methods=['PUT'], strict_slashes=False)
@swag_from('apidoc/put_ticket.yml') # todo write documentation
def put_ticket(ticket_id):
    """ Updates a ticket """
    try:
        original = Tickets.objects.get(id=ticket_id)        
    except DoesNotExist:
        abort(404, description="Given ticket_id is not found")

    updated = request.get_json()
    if not updated:
        abort(400, description='Given object is not a valid JSON')

    print(type(updated))
    
    st_updates(original, updated)
    return Tickets.objects.get(id=ticket_id).to_json()
    
