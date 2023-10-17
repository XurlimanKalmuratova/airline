from django.contrib.admin import *

from .models import Flight
@register(Flight)

class FlightAdmin(ModelAdmin):
    list_display = ('id', 'from1')
    list_display_links = ('id', 'from1')
    
