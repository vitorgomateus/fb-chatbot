import os
import json

import requests
from woocommerce import API

from util import logar
from outway import send_webview


def get_send_products(category, recipient):
    logar("NO* REQUEST PRODUCTS cat={cate}".format(cate=category))

    #ffjfjfjfjvjksdir gdjhkvfhdghvdv,tcj, kgr,ggr gxx jfjfvaonron



    #fkcnvnv

    wc_api_mfip = API(
        url="https://myfriendsinportugal.com",
        consumer_key= os.environ["WC_CONSUMER_KEY"],
        consumer_secret= os.environ["WC_CONSUMER_SECRET"],
        wp_api=True,
        version="wc/v2",
        query_string_auth=True 
    )
            #query_string_auth=True // Force Basic Authentication as query string true and using under HTTPS

    w = wc_api_mfip.get("products?status=publish&filter[lang]=pt")
            #"name": "Ship Your Idea",

            #"permalink": "https://example.com/product/ship-your-idea-22/",
            # "images": [
            # "src": "https://example.com/wp-content/uploads/2017/03/T_4_front-11.jpg",
    response_products = w.json()
    logar("WC_RESPONSE ? ")
    logar(response_products[0]["name"])
    #logar(w.text)


    ### HTTP REQUEST for getting products?
                                            # params = {
                                            #     "access_token": os.environ["PAGE_ACCESS_TOKEN"]
                                            # }
                                            # headers = {
                                            #     "Content-Type": "application/json"
                                            # }
                                            # data = json.dumps({
                                            #     "recipient": {
                                            #         "id": recipient_id
                                            #     },
                                            #     "message":{
                                            #         "text": message_text
                                            #     }
                                            # })
                                            
                                            # wcp = requests.post("https://myfriendsinportugal.com/wp/v2/posts", params=params, headers=headers, data=data)
                                            # if wcp.status_code != 200:
                                            #     logar(wcp.status_code)
                                            #     logar(wcp.text)


    #arr_title=[response_products[0]["name"], response_products[1]["name"], response_products[2]["name"]]
    
    #arr_image=[response_products[0]["images"][0]["src"], response_products[1]["images"][0]["src"], response_products[2]["images"][0]["src"]]
    
    #arr_link=[response_products[0]["permalink"], response_products[1]["permalink"], response_products[2]["permalink"]]
    
    send_webview( arr_title, arr_image, arr_link, recipient)