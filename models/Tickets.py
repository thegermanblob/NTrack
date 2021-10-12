from datetime import datetime
import mongoengine
from mongoengine.fields import DateTimeField
from models.Client import Client
from models.User import User
from models.StatusUpdate import StatusUpdates
mon = mongoengine

class Tickets(mon.Document):
    """ Represents the ticket document of our db"""
    client_id = mon.ReferenceField(Client)
    status = mon.StringField(max_length=10, required=True)
    description = mon.StringField(max_length=150)
    created_by =  mon.ReferenceField(User)
    status_updates = mon.EmbeddedDocumentListField(StatusUpdates)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)

    meta = {
        'collection':"Tickets"
    }