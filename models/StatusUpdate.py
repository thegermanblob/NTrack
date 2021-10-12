from mongoengine.document import EmbeddedDocument
from mongoengine.fields import ReferenceField, StringField
from models.User import User
import mongoengine

class StatusUpdates(EmbeddedDocument):
    """ Class that represents a status update """
    created_by = ReferenceField(User, required=True)
    description = StringField(max_length=400, requiered=True)

    meta = {
        'collection':'StatusUpdates'
    }