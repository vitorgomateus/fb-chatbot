import os
import json

import requests
from woocommerce import API

from util import logar
from outway import send_message

import string

def get_send_products(category, recipient):
    
    max_nop = 3

    #---------------------------------------------------------------------------------WOOCOMMERCE PyPa
    logar("REQUEST PRODUCTS *WC_PyPa* cat={cate}".format(cate=category))
    wc_api_mfip = API(
        url="https://myfriendsinportugal.com",
        consumer_key= os.environ["WC_CONSUMER_KEY"],
        consumer_secret= os.environ["WC_CONSUMER_SECRET"],
        wp_api=True,
        version="wc/v2",
        query_string_auth=True 
    )
        #query_string_auth=True // Force Basic Authentication as query string true and using under HTTPS

    w = wc_api_mfip.get("products?status=publish&per_page=5")
     
    response_products = w.json()
    logar("WC_RESPONSE ? ")
    logar(response_products[0]["name"])
    #logar(type(w))
    #logar(w.text)



    #arr_title=[, response_products[1]["name"], response_products[2]["name"]]
    
    #arr_image=[, response_products[1]["images"][0]["src"], response_products[2]["images"][0]["src"]]
    
    #arr_link= [response_products[0]["permalink"], , response_products[2]["permalink"]]
    
    element = {}
    arr_elements = []
    for i in range(0, max_nop):
        element = {
                    "title":response_products[i]["name"],
                    "image_url":response_products[i]["images"][0]["src"],
                    "subtitle":"",
                    "buttons":[
                        {
                            "type":"web_url",
                            "url":response_products[i]["permalink"],
                            "title":"Read More"
                          }          
                    ]      
                  }
        logar("element{num}".format(num=i))
        logar(element)
        arr_elements.append(element)

    logar("OOO - arr_elements")
    logar(arr_elements)

    send_message( arr_elements, recipient)