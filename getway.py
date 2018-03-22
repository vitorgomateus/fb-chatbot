import os
import json

import requests
from woocommerce import API

from util import logar
from outway import send_webview


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

    w = wc_api_mfip.get("products?status=publish")
     
    response_products = w.json()
    logar(response_products[0]["name"])
    logar("WC_RESPONSE ? ")
    logar(type(w))
    logar(w.text)

    #----------------------------------------------------------------------------------REQUESTS PyPa
    # logar("REQUEST PRODUCTS *REQUESTS* cat={cate}".format(cate=category))
    # params = {
    #     "access_token": os.environ["PAGE_ACCESS_TOKEN"]
    # }
    # headers = {
    #     "Content-Type": "application/json"
    # }
    # data = json.dumps({
    #     url="https://myfriendsinportugal.com",
    #     consumer_key= os.environ["WC_CONSUMER_KEY"],
    #     consumer_secret= os.environ["WC_CONSUMER_SECRET"],
    #     wp_api=True,
    #     version="wc/v2",
    #     query_string_auth=True 
    # })
    
    # wcp = requests.post("https://myfriendsinportugal.com/wp/v2/posts", params=params, headers=headers, data=data)
    
    # logar("WC_REUQESTS_RESPONSE ? ")
    # # logar(response_products[0]["name"])
    # logar(wcp.text)
    # if wcp.status_code != 200:
    #     logar(wcp.status_code)
    #     logar(wcp.text)


    #arr_title=[response_products[0]["name"], response_products[1]["name"], response_products[2]["name"]]
    
    #arr_image=[response_products[0]["images"][0]["src"], response_products[1]["images"][0]["src"], response_products[2]["images"][0]["src"]]
    
    #arr_link=[response_products[0]["permalink"], response_products[1]["permalink"], response_products[2]["permalink"]]
    
    #send_webview( arr_title, arr_image, arr_link, recipient)