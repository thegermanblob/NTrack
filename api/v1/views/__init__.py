""" Blue print for API """
from flask import Blueprint




from api.v1.views.Index import *
from api.v1.views.Tickets import *
from api.v1.views.User import *
from api.v1.views.Clients import *
from api.v1.views.Login import *