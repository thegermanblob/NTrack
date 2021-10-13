""" Module containing all RESTful api actions for Tickets """
from api.v1.app import app_views
from flasgger import swag_from
from flask import jsonify
from models.Client import Client
from models.Tickets import Tickets
from models.User import User

@app_views.route('/tickets', strict_slashes=False)
@swag_from('apidoc/all_tickets.yml')
def all_tickets():
    """ Returns all tickets """ 
    return Tickets.objects.to_json()


#@app_views.route('/tickets/<status>', strict_slashes=False)
#@swag_from('apidoc/ticketstatus.yml')