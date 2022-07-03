
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('living/', views.living_room),
    path('kitchen/', views.kitchen),
    path('bathroom/', views.bathroom),
    path('bedroom/', views.bedroom)
] 