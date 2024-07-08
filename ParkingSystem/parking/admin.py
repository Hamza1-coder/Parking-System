from django.contrib import admin
from .models import Vehicle, ParkingSpot, Ticket

# Register your models here.
admin.site.register(Vehicle)
admin.site.register(ParkingSpot)
admin.site.register(Ticket)