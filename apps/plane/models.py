from django.db import models
from django.db.models import *
from django.contrib.auth.models import AbstractUser

class Plane(Model):
    name = CharField(max_length=256)
    bio = TextField(blank=True, null=True)
    capacity = IntegerField()

    def __str__(self):
        return self.name
    
