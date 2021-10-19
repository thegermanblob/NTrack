""" Blue print for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')



from api.v1.views.Index import *
from api.v1.views.Tickets import *
from api.v1.views.User import *
from api.v1.views.Clients import *