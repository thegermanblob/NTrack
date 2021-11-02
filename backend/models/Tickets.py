from datetime import date, datetime
import mongoengine
from mongoengine.fields import DateTimeField, StringField
from models.Client import Client
from models.User import User
from models.StatusUpdate import StatusUpdates
mon = mongoengine
STATUS =('open','closed','inprogress', 'Open', 'Closed')

class Tickets(mon.Document):
    """ Represents the ticket document of our db"""
    client_id = mon.ReferenceField(Client)
    status = mon.StringField(choices=STATUS, required=True)
    device = mon.StringField()
    description = mon.StringField(max_length=300)
    created_by =  mon.ReferenceField(User)
    status_updates = mon.EmbeddedDocumentListField(StatusUpdates)
    created_at = StringField(default=datetime.utcnow().strftime('%B %d %Y - %H:%M:%S'))
    updated_at = StringField(default=datetime.utcnow().strftime('%B %d %Y - %H:%M:%S'))

    meta = {
        'collection':"Tickets"
    }

    def updated_save(self):
        """ Saves obj and updates updated_at attribute"""
        self.updated_at = datetime.utcnow()
        self.save()

