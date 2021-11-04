from flasgger.utils import swag_from
from flask import Blueprint
from flask import request, abort, session, redirect
from flask.helpers import url_for
from mongoengine.errors import DoesNotExist, ValidationError
from models.User import User
import json
from pprint import pprint
from api.v1.views.Index import app_views
from models.sessions import msessions

@app_views.route('/login', methods=['GET', 'POST'])
@swag_from('apidoc/login.yml')
def login():
    """ The endpoint to login into out service """
    if request.method == 'POST':
        info = request.get_json()
        if not info:
            abort(400, description="Not a Valid JSON")
        if "email" not in info.keys():
            abort(400, description="JSON must include Email")
        try:
            user = User.objects.get(email=info['email'])
        except DoesNotExist:
            abort(400, description="Email does not exist")

        if info['password'] == user.password:
            session['email'] = user.email
            bob = {}
            bob['string']= (str(session.__dict__))
            msessions(bob)

            
            return "Login success"
        else:
            return "Incorrect password"
    else:
        try:
            session['email'] = "hi"
        except:
            return "login page"
        return "login page"