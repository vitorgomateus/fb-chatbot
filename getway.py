import os
import json

import requests
from woocommerce import API

from util import logar
from outway import send_webview

from string import replace


def get_send_products(category, recipient):
    

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
    logar(response_products[0]["name"])
    logar("WC_RESPONSE ? ")
    #logar(type(w))
    logar(w.text)



    arr_title=[response_products[0]["name"], response_products[1]["name"], response_products[2]["name"]]
    
    arr_image=[response_products[0]["images"][0]["src"], response_products[1]["images"][0]["src"], response_products[2]["images"][0]["src"]]
    
   # arr_link= [response_products[0]["permalink"], response_products[1]["permalink"], response_products[2]["permalink"]]
    arr_link= [string.replace(response_products[0]["permalink"], ".jpg", "-300x300.jpg"), 
        string.replace(response_products[1]["permalink"], ".jpg", "-300x300.jpg"), 
        string.replace(response_products[0]["permalink"], ".jpg", "-300x300.jpg")
    ]
    send_webview( arr_title, arr_image, arr_link, recipient)