from datetime import datetime
from mongoengine.document import Document
from mongoengine.fields import DateField, DateTimeField, StringField

class User(Document):
    """ Class that represents a user """
    email = StringField(max_length=50, unique=True)
    password = StringField()
   #user_type  = StringField()
    name = StringField(max_length=15)
    last_name = StringField(max_length=20)
    phone = StringField()
    last_login = DateField()
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)

    meta = {
        'collection':'users'
    }
