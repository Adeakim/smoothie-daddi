from django.urls import path
from django.urls import path
from . import views

urlpatterns=[
    path('', views.home,name='smoothie-home'),
    path('checkout/', views.checkout,name='checkout'),
    path('about/', views.about,name='about'),
    path('cart/',views.cart, name='cart'),
    path('store/',views.store, name='store'),
    path('update-item/',views.updateItems, name='update-item'),
]