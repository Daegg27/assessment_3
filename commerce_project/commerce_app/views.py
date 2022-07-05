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

    auth = OAuth1("8bab92f001234e7ebcedf97e9281e439", "af62b1cff2154c6f84fc99610bc5002a")

    kitchen_appliances = []

    # for item in user_interactions: #////////////////////////THIS IS THE REAL METHOD I WILL USE
    #     if item['tag'] == 'kitchen':
    #         endpoint = f"http://api.thenounproject.com/icon/{item['name']}"
    #         response = HTTP_Client.get(endpoint, auth=auth)
    #         responseJSON = response.json()
    #         item['display_image'] = responseJSON['icon']['preview_url']
    #         kitchen_appliances.append(item) # Easily lets me know which items need to actually be shown on this page
    # print(kitchen_appliances)

    for item in user_interactions:
        if item['tag'] == 'kitchen':
            kitchen_appliances.append(item)

    my_data = {
        'kitchen_appliances': kitchen_appliances
    }

    return render(request, 'kitchen.html', my_data)

def bedroom(request):

    auth = OAuth1("8bab92f001234e7ebcedf97e9281e439", "af62b1cff2154c6f84fc99610bc5002a")

    bedroom_appliances = []

    # for item in user_interactions: #////////////////////////THIS IS THE REAL METHOD I WILL USE
    #     if item['tag'] == 'bedroom':
    #         endpoint = f"http://api.thenounproject.com/icon/{item['name']}"
    #         response = HTTP_Client.get(endpoint, auth=auth)
    #         responseJSON = response.json()
    #         item['display_image'] = responseJSON['icon']['preview_url']
    #         bedroom_appliances.append(item) # Easily lets me know which items need to actually be shown on this page
    # print(bedroom_appliances)

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
