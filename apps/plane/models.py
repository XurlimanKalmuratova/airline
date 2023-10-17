from django.db import models
from django.db.models import *

class Plane(Model):
    name = CharField(max_length=256)
    bio = TextField(blank=True, null=True)
    capacity = IntegerField()

    def __str__(self):
        return self.name
    
    