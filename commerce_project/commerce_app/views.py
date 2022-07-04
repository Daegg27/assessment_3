from http.client import responses
import json
import re
from django.shortcuts import render
from urllib import response
import requests as HTTP_Client
from requests_oauthlib import OAuth1



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
    }
]



# Create your views here.
def index(request):

  
    return render(request, 'index.html')

def living_room(request):

    auth = OAuth1("8bab92f001234e7ebcedf97e9281e439", "af62b1cff2154c6f84fc99610bc5002a")

    living_appliances = []

    # for i in range(0, 3): 
    #     endpoint = f"http://api.thenounproject.com/icon/{user_interactions[i]['name']}"
    #     response = HTTP_Client.get(endpoint, auth=auth)
    #     responseJSON = response.json()
    #     display_images.append(responseJSON['icon']['preview_url'])
    # print(display_images)


    # for item in user_interactions: ////////////////////////THIS IS THE REAL METHOD I WILL USE
    #     if item['tag'] == 'living':
    #         endpoint = f"http://api.thenounproject.com/icon/{item['name']}"
    #         response = HTTP_Client.get(endpoint, auth=auth)
    #         responseJSON = response.json()
    #         item['display_image'] = responseJSON['icon']['preview_url']
    #         living_appliances.append(item) # Easily lets me know which items need to actually be shown on this page
    # print(living_appliances)

    for item in user_interactions:
        if item['tag'] == 'living':
            living_appliances.append(item)

    my_data = {
        'living_appliances': living_appliances
    }


    return render(request, 'living_room.html', my_data)

def kitchen(request):

    return render(request, 'kitchen.html')

def bedroom(request):

    return render(request, 'bedroom.html')

def bathroom(request):

    return render(request, 'bathroom.html')

def search(request):

    return render(request, 'search.html')

def cart(request):

    return render(request, 'cart.html')
