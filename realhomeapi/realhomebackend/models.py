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


class NewRealEstate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    address = models.CharField(max_length=500)
    bathrooms = models.IntegerField(default=0)
    bedrooms = models.IntegerField(default=0)
    type_id = models.ForeignKey(RealEstateType, on_delete=models.CASCADE)
    minPrice=models.IntegerField(default=0)
    maxPrice=models.IntegerField(default=0)
    dateCreated = models.DateTimeField(default=django.utils.timezone.now)

    class Meta:
        db_table = 'new_real_estates'
        managed = True  
    
    


    

    

       
        





