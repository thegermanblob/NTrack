from datetime import datetime
from mongoengine.document import Document
from mongoengine.fields import DateTimeField, StringField

class Client(Document):
    """ Class representation of a client """
    client_name = StringField(max_length=15, required=True)
    client_last_name = StringField(max_length=20, required=True)
    client_email = StringField(max_length=50, unique=True)
    client_phone = StringField(max_length=15)
    address = StringField(max_length=100)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection':'Clients'
    }