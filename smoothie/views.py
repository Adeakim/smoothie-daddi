from django.shortcuts import render
from django.http import JsonResponse
import datetime
import json

from .models import *
from .utils import cookieCart,cartData,guestOrder



def home(request):
    data = cartData(request)
    cartItems = data['cartItems']    

       
    products=Products.objects.all()
    context={'products':products,'cartItems':cartItems}
    return render(request,'smoothie/index.html',context)
    

def checkout(request):
    
    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']    

    context={'items':items,'order':order,'cartItems':cartItems}
    return render(request,'smoothie/checkout.html',context)


def about(request):
    return render(request,'smoothie/about.html')

def cart(request):
    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']    

            
    context={'items':items,'order':order,'cartItems':cartItems}
    return render(request, 'smoothie/cart.html',context)

def store(request):
    data = cartData(request)
    cartItems = data['cartItems']    

       
    products=Products.objects.all()
    context={'products':products,'cartItems':cartItems}
    return render(request,'smoothie/store.html',context)
    

def updateItems(request):
    data = json.loads(request.body)
    productid = data['productid']
    action = data['action']

    print('action:', action)
    print('productId:', productid)
    customer= request.user.customer
    product = Products.objects.get(id=productid)
    order,created = Order.objects.get_or_create(customer=customer,complete=False) 
    orderItem,created = OrderItem.objects.get_or_create(order=order,product=product) 

    if action == 'add':
        orderItem.quantity=(orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity=(orderItem.quantity - 1)

    orderItem.save()
    
    if orderItem.quantity <=0:
        orderItem.delete()

    return JsonResponse("Item was added",safe=False)

def payment(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['userForm']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)
    





    
