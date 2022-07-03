import re
from django.shortcuts import render
from urllib import response
import requests as HTTP_Client

# Create your views here.
def index(request):
    
    return render(request, 'index.html')
