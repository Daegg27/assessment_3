
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('living/', views.living_room),
    path('kitchen/', views.kitchen),
    path('bedroom/', views.bedroom),
    path('search/', views.search),
    path('cart/', views.cart),
    path('products', views.products)
] 