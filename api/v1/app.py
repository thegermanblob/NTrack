""" Flask aplication """
from flask import Flask
from flasgger import Swagger
from api.v1.views import app_views
from models.mongo_setup import global_init
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'
app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origins": "*"}})

Swagger(app)

if __name__ == "__main__":
    """ Main function """
    host = "0.0.0.0"
    port = "5000"
    global_init()
    app.run(host=host, port=port, threaded=True)