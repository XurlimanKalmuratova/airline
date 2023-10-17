from django.db.models import *
from apps.plane.models import Plane
class Airline(Model):
    name = CharField(max_length=256)
    created_at = DateField()
    planes = ForeignKey(Plane, on_delete=CASCADE)


    def __str__(self):
        return self.name
    
