from datetime import datetime
from mongoengine.document import Document
from mongoengine.fields import DateField, ReferenceField, StringField
from models.User import User
import mongoengine

class msessions(Document):
    """ Class that represents a session """
    string = StringField()
