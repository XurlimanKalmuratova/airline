from django.db.models import *
from apps.plane.models import Plane
from apps.airline.models import Airline

class Flight(Model):
    from1 = CharField(max_length=256)
    to = CharField(max_length=256)
    plane = ForeignKey(Plane, on_delete=CASCADE)
    airline = OneToOneField(Airline, on_delete=CASCADE)
    price = PositiveIntegerField()


    def __str__(self):
        return self.from1