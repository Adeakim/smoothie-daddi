from django.db import models
from django.contrib.auth.models import User
import uuid


from django.db.models.deletion import CASCADE


class Customer(models.Model):
    customer=models.OneToOneField(User, null=True, on_delete=models.CASCADE,blank=True)
    name = models.CharField(max_length=200)
    email=models.EmailField(max_length=200)

    def __str__(self):
        return self.name

class Products(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    name=models.CharField(max_length=50)
    about=models.TextField()
    price= models.FloatField()
    image=models.ImageField(upload_to='Product_pics')
    digital = models.BooleanField(default=False,null=True,blank=False)
    
    def __str__(self):
        return self.name
    


class Order(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    customer=models.ForeignKey(Customer, null=True,on_delete=models.SET_NULL,blank=True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    product_id=models.ForeignKey(Products,on_delete=CASCADE)
    transaction_id = models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True,)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping= False
        orderitems=self.orderitem_set.all()
        for item in orderitems:
            if item.product.digital ==False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total= sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems=self.orderitem_set.all()
        total= sum([item.quantity for item in orderitems])
        return total
    
class OrderItem(models.Model):
    product=models.ForeignKey(Products,on_delete=models.SET_NULL,null=True,blank=True)
    order= models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(null=True,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} ({str(self.quantity)})"
        

    @property
    def get_total(self):
        total = self.product.price *  self.quantity
        return total


class ShippingAddress(models.Model):
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    order = models.ForeignKey(Order,null=True,on_delete=models.SET_NULL)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    zipcode=models.CharField(max_length=200,null=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
