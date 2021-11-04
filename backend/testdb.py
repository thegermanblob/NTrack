from mongoengine import *
from mongoengine.connection import connect
from mongoengine import Document, DateField
from mongoengine.fields import StringField

class Bob(Document):
    """ Class that represents a user """
    email = StringField(max_length=50, unique=True)
    password = StringField()
    #user_type  = StringField()
    name = StringField(max_length=15)
    last_name = StringField(max_length=20)
    phone = StringField()
    last_login = DateField()

#class User(Document):
#    email = StringField(required=True)
#    name = StringField(max_length=50)
#    last_name = StringField(max_length=50)


connect('NTrack')

ros = Bob(email='bobasd',name='asd', last_name='bob').save()
for i in Bob.objects.all():
    print(i)