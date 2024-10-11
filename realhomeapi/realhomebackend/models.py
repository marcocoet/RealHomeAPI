import django.utils.timezone
from django.db import models
import uuid

class RealEstateType(models.Model):
    Id = models.UUIDField(primary_key=True)
    Name = models.CharField(max_length=50)
    DisplayName = models.CharField(max_length=100)
    DateCreated = models.DateTimeField()

    class Meta:
        db_table = 'real_estate_types'
        managed = False

class Users(models.Model):
    Username = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=15)
    
    class Meta:
        db_table = 'users'
        managed = False

class RealEstate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    address = models.CharField(max_length=500)
    bathrooms = models.IntegerField(default=0)
    bedrooms = models.IntegerField(default=0)
    #type_id = models.ForeignKey(RealEstateType, on_delete=models.CASCADE)
    landSqm = models.IntegerField(default=0)
    floorSqm = models.IntegerField(default=0)
    parking = models.IntegerField(default=0)
    shortDescription = models.CharField(max_length=250, default="")
    longDescription = models.CharField(max_length=50000, default="")
    dateCreated = models.DateTimeField(default=django.utils.timezone.now)

    class Meta:
        db_table = 'real_estates'
        managed = False

    
