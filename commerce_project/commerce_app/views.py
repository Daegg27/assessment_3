import re
from django.shortcuts import render
from urllib import response
import requests as HTTP_Client

# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def living_room(request):
    
    return render(request, 'living_room.html')

def kitchen(request):

    return render(request, 'kitchen.html')

def bedroom(request):

    return render(request, 'bedroom.html')

def bathroom(request):

    return render(request, 'bathroom.html')
