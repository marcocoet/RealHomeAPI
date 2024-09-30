from django.db import models

class RealEstateType(models.Model):
    Id = models.UUIDField(primary_key=True)
    Name = models.CharField(max_length=50)
    DisplayName = models.CharField(max_length=100)
    DateCreated = models.DateTimeField()

    class Meta:
        db_table = 'real_estate_types'
        managed = False

class Users(models.Model):
    Id = models.UUIDField(primary_key=True)
    Name = models.CharField(max_length=50)
    Surname= models.CharField(max_length=50)
    Password= models.CharField(max_length=50)
    DateCreated = models.DateTimeField()