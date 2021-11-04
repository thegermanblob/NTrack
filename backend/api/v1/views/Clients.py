""" Module containing all RESTful api actions for Clients """
from flask import abort, json, request, Blueprint
from flasgger.utils import swag_from, validate
from mongoengine.errors import DoesNotExist, NotUniqueError, ValidationError
from models.Client import Client
from api.v1.views.Index import app_views



@app_views.route('/clients', methods=['GET'], strict_slashes=False)
@swag_from('apidoc/all_clients.yml')
def all_clients():
    """ Returns all clients"""
    return Client.objects.to_json()

@app_views.route('/client/<client_id>',methods=['GET'], strict_slashes=False)
@swag_from('apidoc/get_client.yml')
def get_client(client_id):
    """ Gets Client from the data base """
    try:
        return Client.objects.get(id=client_id).to_json()
    except DoesNotExist:
        abort(404, description="Client_id does not exist")
    except ValidationError:
        abort(404, description="Invalid Id")

@app_views.route('/clients/', methods=['POST'], strict_slashes=False)
@swag_from('apidoc/post_client.yml')
def post_client():
    """ Takes a client json and adds it to the Database """
    new = request.get_json()
    if not new:
        abort(404, description="Not a JSON")
    
    new.pop('_id', None)
    new = Client(**new)
    try:
        new.save()
    except NotUniqueError:
        abort(400, description="Not a unique email")
    return (new.to_json())


@app_views.route('/clients/<client_id>', methods=['PUT'], strict_slashes=False)
@swag_from('apidoc/put_client.yml')
def put_client(client_id):
    """ Updates a client """
    try:
        original = Client.objects.get(id=client_id)
    except DoesNotExist:
        abort(404, description= 'Given client_id does not exist')

    updated = request.get_json()
    if not updated:
        abort(404, description="Given object not a valid json")

    updated.pop('_id', None)
    original.update(**updated)
    original = Client.objects.get(id=client_id)
    return original.to_json()