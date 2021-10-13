""" Index """
from flasgger import swag_from
from flask import jsonify
from api.v1.app import app_views
from models.Tickets import Tickets
from models.User import User
from models.Client import Client

@app_views.route('/status', methods=['GET'], strict_slashes=False)
@swag_from('./apidoc/status.yml')
def status():
    """ Status of API """
    return jsonify({"status":"OK"})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
@swag_from('./apidocs/stats.yml')
def stats():
    """ Returns the number of each objects by type """
    clases = { "Tickets":Tickets, "Users":User, "Clients":Client}

    count = {}
    for key, value in clases.items():
        count[key] = value.objects.count()

    return jsonify(count)