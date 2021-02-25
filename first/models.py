from django.db import models


# Create your models here.
class Vehicle(models.Model):
    TROPICAL = 'Tropical'
    DRY = 'Dry'
    TEMPERATE = 'Temperate'
    CONTINENTAL = 'Continental'
    POLAR = 'Polar'
    CLIMATE_CHOICES = [
        (TROPICAL, 'Tropical'),
        (DRY, 'Dry'),
        (TEMPERATE, 'Temperate'),
        (CONTINENTAL, 'Continental'),
        (POLAR, 'Polar'),
    ]

    name = models.CharField(blank=False, max_length=120, help_text="* Eks: BMW I3 2009, Airbus A319", null=True)
    mode_of_transport = models.CharField(blank=False, max_length=30, help_text="* Eks: Car, Plane", null=True)
    engine = models.FloatField(blank=True, null=True, help_text="Engine size in liter")
    fuel = models.CharField(blank=True, max_length=120, help_text="Eks: Electric, Diesel", null=True)
    drag = models.FloatField(blank=True, help_text="Newtons", null=True)
    climate = models.CharField(blank=True, choices=CLIMATE_CHOICES, max_length=120, null=True)
    weight = models.IntegerField(blank=True, help_text="Kg", null=True)
    passengers = models.IntegerField(blank=True, null=True)
    attachments = models.FileField(blank=True, null=True)
    comment = models.TextField(blank=True, max_length=300, null=True)

    def __ser__(self):
        return self.name
