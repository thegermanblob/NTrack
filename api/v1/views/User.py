""" Model containing all RESTful api action for Users """
from flask import abort, request, Blueprint
from flasgger.utils import swag_from
from flask import json
from mongoengine.errors import DoesNotExist, ValidationError
from models.User import User
from api.v1.views.Index import app_views

@app_views.route('/users', methods=['GET'], strict_slashes=False)
@swag_from('apidoc/all_users.yml')
def all_users():
    """ Returns all users """
    return User.objects.to_json()

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
@swag_from('apidoc/get_user.yml')
def get_user(user_id):
    """ Gets user with given user id """
    try:
        return User.objects.get(id=user_id)
    except DoesNotExist:
        abort(404, description="Given user id does not exists")
    except ValidationError:
        abort(404, description="Invalid id")


@app_views.route('/users/', methods=['POST'], strict_slashes=False)
@swag_from('apidoc/post_user.yml')
def post_user():
    """ Takes a user json object and adds it to the database"""
    new = request.get_json()
    if not new:
        abort(400, description="Not a valid Json")
    
    new = json.loads(new)
    new.pop('_id', None)
    new = User(**new)
    new.save()
    return (new.to_json())

@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
@swag_from('apidoc/put_user.yml')
def put_user(user_id):
    """ Updates user """
    try:
        original: User.objects.get(id=user_id)
    except DoesNotExist:
        abort(404, description="Given users_id does not exist")
    
    updated = request.get_json()
    if not updated:
        abort(404, description="Given object is not a valid json")

    original.update(**updated)
    return original.to_json()