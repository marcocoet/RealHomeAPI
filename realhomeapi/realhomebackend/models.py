from django.db import models


class RealEstateType(models.Model):
    Id = models.UUIDField(primary_key=True)
    Name = models.CharField(max_length=50)
    DisplayName = models.CharField(max_length=100)
    DateCreated = models.DateTimeField()

    class Meta:
        db_table = 'real_estate_types'
        managed = False

class Realestate_All_Buy(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    suburb = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    

    class Meta:
        db_table = 'allrealestatesbuy'
        managed = False
