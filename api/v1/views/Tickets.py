""" Module containing all RESTful api actions for Tickets """
from mongoengine.errors import DoesNotExist, FieldDoesNotExist, ValidationError
from api.v1.app import app_views
from flasgger import swag_from
from flask import json, jsonify, request, abort
from models.Client import Client
from models.Tickets import Tickets
from models.User import User

@app_views.route('/tickets', methods=['GET'], strict_slashes=False)
@swag_from('apidoc/all_tickets.yml')
def all_tickets():
    """ Returns all tickets """ 
    return Tickets.objects.to_json()


@app_views.route('/tickets/<tstatus>', strict_slashes=False)
@swag_from('apidoc/ticketstatus.yml')
def ticket_status(tstatus):
    """ Returns tickets that match status """
    return Tickets.objects(status=tstatus).to_json()

@app_views.route('/tickets', methods=['POST'], strict_slashe=False)
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



@app_views.route('/tickets/<ticket_id>', methods=['PUT'], strict_slashes=False)
@swag_from('apidoc/put_ticket.yml')
def put_ticket(ticket_id):
    """ Updates a ticket """
    try:
        original = Tickets.objects.get(id=ticket_id)        
    except DoesNotExist:
        abort(404, description="Given ticket_id is not found")

    updated = request.get_json()
    if not updated:
        abort(400, description='Given object is not a valid JSON')

    try:
        updated = Tickets.from_json(updated)
    except FieldDoesNotExist:
        abort(400, description="One of given fields is incorrect")
    
    try:
        updated.updated_save()
    except ValidationError:
        abort(400,description="Missing required field")
