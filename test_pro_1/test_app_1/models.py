from __future__ import unicode_literals

from mongoengine import *
from test_pro_1.settings import DBNAME

connect(DBNAME)
# Create your models here.
class TestModel(Document):
    name = StringField(required=True)
    age = IntField(requred=False)
    
