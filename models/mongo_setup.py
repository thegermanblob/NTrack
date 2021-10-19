import mongoengine
from mongoengine.connection import connect

def global_init():
    uri = "mongodb+srv://testconsole:Miniclip1@ntrack.chjv9.mongodb.net/Ntrack?retryWrites=true&w=majority"
    #for cloud database use uri for local use 'Ntrack'
    connect(host=uri)