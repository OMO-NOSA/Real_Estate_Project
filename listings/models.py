from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listings(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200, default='welcome')
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_one = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_two = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_three = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_four = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_five = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_six = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title



