from django.db import models
import uuid

from django.db.models.deletion import CASCADE


class Products(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    name=models.CharField(max_length=50)
    about=models.TextField()
    price= models.FloatField()
    image=models.ImageField(upload_to='Product_pics')
    
    def __str__(self):
        return self.name
    

class Booking(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    product_id=models.ForeignKey(Products,on_delete=CASCADE)
    
    
    def __str__(self):
        return self.id
    
