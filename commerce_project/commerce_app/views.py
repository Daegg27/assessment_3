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
        'price': 75.99,
        'display_image': "https://static.thenounproject.com/png/10737-200.png"
    },
    {
        'tag': 'living',
        'name': 'Table',
        'price': 29.99,
        'display_image': "https://static.thenounproject.com/png/1392-200.png"
    },
    {
        'tag': 'living',
        'name': 'Bookshelf',
        'price': 59.99,
        'display_image': "https://static.thenounproject.com/png/19087-200.png"
    },
    {
        'tag': 'kitchen',
        'name': 'Refrigerator',
        'price': 119.99,
        'display_image': "https://static.thenounproject.com/png/1859-200.png"
    },
    {
        'tag': 'kitchen',
        'name': 'Sink',
        'price': 49.99,
        'display_image': "https://static.thenounproject.com/png/7581-200.png"
    },
    {
        'tag': 'kitchen',
        'name': 'Microwave',
        'price': 34.99,
        'display_image': "https://static.thenounproject.com/png/10744-200.png"
    },
    {
        'tag': 'bedroom',
        'name': 'Bed',
        'price': 149.99,
        'display_image': "https://static.thenounproject.com/png/1072-200.png"
    },
    {
        'tag': 'bedroom',
        'name': 'Drawer',
        'price': 49.99,
        'display_image': "https://static.thenounproject.com/png/23609-200.png"
    },
    {
        'tag': 'bedroom',
        'name': 'Television',
        'price': 119.99,
        'display_image': "https://static.thenounproject.com/png/416-200.png"
    },
    {
        'tag': 'cart',
        'name': 'username',
        'items_ordered': [],
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
            living_appliances.append(item) # Found this to be a good way to consolidate and keep it simple and uniformed throughout the program. 

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


    item_names = user_interactions[9]['items_ordered']
    price = round(user_interactions[9]['order_cost'], 2)
    quantity = user_interactions[9]['quantity']
    



    my_data = {
        'item_names': item_names,
        'price': price,
        'quantity': quantity
    }

    return render(request, 'cart.html', my_data)

def products(request):
    
    query = request.GET.get('query')

    for items in user_interactions:
        if query.upper() == items['name'].upper():
            # return redirect('/commerce/') # Couldn't get this to work, tried multiple methods, wanted to redirect to the corresponding page if the item was found
            return None


    auth = OAuth1(os.environ['API_KEY'], os.environ['SECRET'])
    endpoint = f"http://api.thenounproject.com/icon/{query}"

    response = HTTP_Client.get(endpoint, auth=auth)
    responseJSON = response.json()

    image_url = responseJSON['icon']['preview_url']
    


    return JsonResponse({'image_url': image_url})

def purchase(request):
    
    itemName = request.GET.get('itemName')

    for items in user_interactions: # Finds the cost of the item added.
        if items['name'] == itemName:
            item_cost = items['price']
            break # There shouldn't be any duplicate items, but just a safety measure
    

    for items in user_interactions: # This will actually add each item to the cart 
        if items['tag'] == 'cart':
            items['items_ordered'].append(itemName)
            items['order_cost'] += item_cost
            items['quantity'] += 1
    # print(user_interactions[9])




    return JsonResponse({'itemName': itemName})