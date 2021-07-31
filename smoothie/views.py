from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json




def home(request):
    products=Products.objects.all()[:2]
    return render(request,'smoothie/index.html',{'products':products})


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False) 
        items = order.orderitem_set.all()
    else:
        items=[]
        order ={'get_cart_items':0, 'get_cart_total':0, 'shipping':False}
    context={'items':items,'order':order}
    return render(request,'smoothie/checkout.html',context)

def about(request):
    products=Products.objects.all()
    return render(request,'smoothie/about.html',{'products':products})

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False) 
        items = order.orderitem_set.all()
    else:
        items=[]
        order ={'get_cart_items':0, 'get_cart_total':0,'shipping':False}

    context={"items":items,"order":order}
    return render(request,"smoothie/cart.html",context)

def store(request):
    products=Products.objects.all()

    return render(request,'smoothie/store.html',{'products':products})

def updateItems(request):
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)
    
    productId = data['productId']
    action = data['action']
    customer = request.user.customer
    product = Products.objects.get(id=productId)
    order,created = Order.objects.get_or_create(customer=customer,complete=False) 
    orderItem,created = OrderItem.objects.get_or_create(order=order,product=product) 

    if action=='add':
        orderItem.quantity +=1
    elif action =='remove':
        orderItem.quantity -=1
    orderItem.save()
     
    if orderItem.quantity<=0:
        orderItem.delete()

    return JsonResponse('Item was added',safe=False)



    
