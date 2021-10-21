""" Index """
from flasgger import swag_from
from flask import jsonify, Blueprint
from models.Client import Client
from models.Tickets import Tickets
from models.User import User

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

@app_views.route('/status', methods=['GET'], strict_slashes=False)
@swag_from('apidoc/status.yml')
def status():
    """ Status of API """
    return jsonify({"status":"OK"})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
@swag_from('apidoc/stats.yml')
def stats():
    """ Returns the number of each objects by type """
    clases = { "Tickets":Tickets, "Users":User, "Clients":Client}

    count = {}
    for key, value in clases.items():
        count[key] = value.objects.count()

    return jsonify(count)
