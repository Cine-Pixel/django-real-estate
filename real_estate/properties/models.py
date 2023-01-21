from django.contrib.auth.models import User
from django.db import models


class Property(models.Model):
    """
    Stores a single property entry, related to :model:`auth.User`.

    """

    title = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    address = models.CharField(max_length=300)
    total_area = models.IntegerField(null=True, blank=True)
    rooms = models.IntegerField(null=True, blank=True)
    bed_rooms = models.IntegerField(null=True, blank=True)
    water = models.BooleanField(default=False)
    internet = models.BooleanField(default=False)
    tv = models.BooleanField(default=False)
    gas = models.BooleanField(default=False)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.title


class Image(models.Model):
    """
    Stores images for properties

    """

    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.FileField(upload_to="images/", default="images/default.png")
