""" Blue print for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')



from api.v1.views.Index import *
from api.v1.views.Tickets import *
#todo from api.v1.views.User import *
#todo from api.v1.views.Client import *