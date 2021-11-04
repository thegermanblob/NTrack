from datetime import datetime
from mongoengine.document import EmbeddedDocument
from mongoengine.fields import DateField, ReferenceField, StringField
from models.User import User
import mongoengine

class StatusUpdates(EmbeddedDocument):
    """ Class that represents a status update """
    created_by = ReferenceField(User, required=True)
    status_change = StringField()
    comment = StringField(max_length=400)
    created = StringField(default=datetime.utcnow().strftime('%B %d %Y - %H:%M:%S'))
