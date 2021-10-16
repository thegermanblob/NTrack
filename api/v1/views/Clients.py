""" Module containing all RESTful api actions for Clients """
from functools import _Descriptor
from flask import abort, json, request
from flasgger.utils import swag_from, validate
from mongoengine.errors import DoesNotExist, ValidationError
from api.v1.views  import app_views
from models.Client import Client


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
        return Client.objects.get(id=client_id)
    except DoesNotExist:
        abort(404, description="Client_id does not exist")
    except ValidationError:
        abort(404, description="Invalid Id")

@app_views.route('/clients/', methods=['POST'], strict_slashes=False)
@swag_from('apidocs/post_client.yml')
def post_client():
    """ Takes a client json and adds it to the Database """
    new = request.get_json()
    if not new:
        abort(404, description="Not a JSON")
    
    new = json.loads(new)
    new.pop('_id', None)
    new = Client(**new)
    new.save()
    return (new.to_json)


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

    original.update(**updated)
    return original.to_json()