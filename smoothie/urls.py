from django.urls import path
from django.urls import path
from . import views

urlpatterns=[
    path('', views.home,name='smoothie-home'),
    path('<uuid:product_id>/booking/', views.booking,name='booking')
]