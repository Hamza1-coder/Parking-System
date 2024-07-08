from django.db import models
from django.utils import timezone

class Vehicle(models.Model):
    VEHICLE_TYPE_CHOICES = [
        ('TW', 'Two Wheeler'),
        ('FW', 'Four Wheeler'),
    ]
    vehicle_number = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=2, choices=VEHICLE_TYPE_CHOICES)
    
class ParkingSpot(models.Model):
    id = models.AutoField(primary_key=True)
    is_empty = models.BooleanField(default=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    entry_time = models.DateTimeField(default=timezone.now)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    parking_spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)