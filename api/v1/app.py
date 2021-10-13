""" Flask aplication """
from flask import Flask
from flasgger import Swagger
from api.v1.views import app_views
from models.mongo_setup import global_init

app = Flask(__name__)
app.register_blueprint(app_views)

Swagger(app)

if __name__ == "__main__":
    """ Main function """
    host = "0.0.0.0"
    port = "5000"
    global_init()
    app.run(host=host, port=port, threaded=True)