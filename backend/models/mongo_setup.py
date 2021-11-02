import mongoengine
from mongoengine.connection import connect

def global_init():
    uri = "mongodb+srv://testconsole:Miniclip1@ntrack.chjv9.mongodb.net/Ntrack?retryWrites=true&w=majority"
    #! change <password> to password
    #for cloud database use host=uri for local use db='Ntrack'
    connect(host=uri)