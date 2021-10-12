import mongoengine
from mongoengine.connection import connect

def global_init():
    connect(db='Ntrack')