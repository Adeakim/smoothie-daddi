from django.shortcuts import render
from .models import Products,Booking


def home(request):
    products=Products.objects.all()
    
    return render(request,'smoothie/index.html',{'products':products})

def booking(request,product_id):
    product_id=Booking.objects.all()
    return render(request,'smoothie/booking.html',{'product_id':product_id})
    
