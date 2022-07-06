from http.client import responses
import json
import re
from django.shortcuts import render, redirect
from urllib import response
import requests as HTTP_Client
from requests_oauthlib import OAuth1
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from dotenv import load_dotenv
import os

load_dotenv()

user_interactions = [
     
     {
        'tag': 'living',
        'name': 'Couch',
        'quantity': 5,
        'price': 75.99,
        'display_image': "https://static.thenounproject.com/png/10737-200.png"
    },
    {
        'tag': 'living',
        'name': 'Table',
        'quantity': 3,
        'price': 29.99,
        'display_image': "https://static.thenounproject.com/png/1392-200.png"
    },
    {
        'tag': 'living',
        'name': 'Bookshelf',
        'quantity': 7,
        'price': 59.99,
        'display_image': "https://static.thenounproject.com/png/19087-200.png"
    },
    {
        'tag': 'kitchen',
        'name': 'Refrigerator',
        'quantity': 4,
        'price': 119.99,
        'display_image': "https://static.thenounproject.com/png/1859-200.png"
    },
    {
        'tag': 'kitchen',
        'name': 'Sink',
        'quantity': 2,
        'price': 49.99,
        'display_image': "https://static.thenounproject.com/png/7581-200.png"
    },
    {
        'tag': 'kitchen',
        'name': 'Microwave',
        'quantity': 6,
        'price': 34.99,
        'display_image': "https://static.thenounproject.com/png/10744-200.png"
    },
    {
        'tag': 'bedroom',
        'name': 'Bed',
        'quantity': 1,
        'price': 149.99,
        'display_image': "https://static.thenounproject.com/png/1072-200.png"
    },
    {
        'tag': 'bedroom',
        'name': 'Drawer',
        'quantity': 4,
        'price': 49.99,
        'display_image': "https://static.thenounproject.com/png/23609-200.png"
    },
    {
        'tag': 'bedroom',
        'name': 'Television',
        'quantity': 3,
        'price': 119.99,
        'display_image': "https://static.thenounproject.com/png/416-200.png"
    },
    {
        'tag': 'cart',
        'items_ordered': {},
        'order_cost': 0,
        'quantity': 0
    }
]



# Create your views here.
def index(request):

  
    return render(request, 'index.html')

def living_room(request):


    living_appliances = []


    for item in user_interactions:
        if item['tag'] == 'living':
            living_appliances.append(item)

    my_data = {
        'living_appliances': living_appliances
    }


    return render(request, 'living_room.html', my_data)

def kitchen(request):


    kitchen_appliances = []


    for item in user_interactions:
        if item['tag'] == 'kitchen':
            kitchen_appliances.append(item)

    my_data = {
        'kitchen_appliances': kitchen_appliances
    }

    return render(request, 'kitchen.html', my_data)

def bedroom(request):


    bedroom_appliances = []

    for item in user_interactions:
        if item['tag'] == 'bedroom':
            bedroom_appliances.append(item)

    my_data = {
        'bedroom_appliances': bedroom_appliances
    }

    return render(request, 'bedroom.html', my_data)


def search(request):

    return render(request, 'search.html')


def cart(request):

    return render(request, 'cart.html')

def products(request):
    

    # print(request.GET.get('query'))
    query = request.GET.get('query')

    for items in user_interactions:
        if query.upper() == items['name'].upper():
            # return redirect('/commerce/') # Couldn't get this to work, tried multiple methods
            return None


    auth = OAuth1(os.environ['API_KEY'], os.environ['SECRET'])
    endpoint = f"http://api.thenounproject.com/icon/{query}"

    response = HTTP_Client.get(endpoint, auth=auth)
    responseJSON = response.json()

    image_url = responseJSON['icon']['preview_url']
    


    return JsonResponse({'image_url': image_url})
