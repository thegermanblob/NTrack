from flasgger.utils import swag_from
import flask
from flask import request, abort, session
from mongoengine.errors import DoesNotExist, ValidationError
from api.v1.views import app_views
from models.User import User

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