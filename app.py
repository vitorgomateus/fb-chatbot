import os
import sys
import json
import time
from datetime import datetime

import requests
from flask import Flask, request
from woocommerce import API
from funcao import senda_message
from util import logar

app = Flask(__name__)


@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello earth, it's alive!!!!", 200


@app.route('/', methods=['POST'])
def webhook():

    # endpoint for processing incoming messaging events

    
    data = request.get_json()
    logar("_DATA_")
    logar(data)  # you may not want to log every incoming message in production, but it's good for testing

    # VTOR
    # if data["object"] == "page":
    #     for entry in data["entry"]:
    #         for messaging_event in entry["messaging"]:
    #             if messaging_event["message"].get("is_echo"):
    #                 logar("WE GOT ECHO")
    #
    #strdata = str(data)
    #strdata= json.dumps(data)
    #if "standby" in strdata:
       #logar("WE HAVE STANBY")
    #
    #time.sleep(300) 
    # if data["object"] == "page":

    #   original
    if data["object"] == "page":
        for entry in data["entry"]:

            if entry.get("standby"):
                for standby_event in entry["standby"]:  # a message was sent in standby
                    logar("STANBY EVENT")

            elif entry.get("messaging"):

                for messaging_event in entry["messaging"]:
                    sender_id_pass = messaging_event["sender"]["id"]

                    if messaging_event.get("message"):  # someone sent us a message
                        sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
                        recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID

                        if messaging_event["message"].get("attachments"):
                            logar("Bot got a sticker!")
                        else:
                            message_text = messaging_event["message"]["text"]  # the message's text
                            if message_text == "produtos":
                                get_send_products(0, sender_id)
                            else:
                               senda_message(sender_id, "BOT :D")
                               pass

                    if messaging_event.get("request_thread_control"):  # ADMIN requested control
                        logar("ADMIN REQUEST CONTROL sender_id={sendr}".format(sendr=sender_id_pass))
                        pass_thread_control(sender_id_pass)

                    if messaging_event.get("request_thread_control"):  # ADMIN control passed
                        logar("PASS CONTROL TO ADMIN")
                        
                    if messaging_event.get("delivery"):  # delivery confirmation
                        pass

                    if messaging_event.get("optin"):  # optin confirmation
                        pass

                    if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                        pass

            else:
                logar("DEVDO - No Standby, neither Messaging")
    else:
        logar("DEVDO - no PAGE")

    return "ok", 200




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



def send_webview(title_arr, img_arr, url_arr, recipient_id):
    logar("NO* SEND_WEBVIEW")
    # iterate through arr...
    paramsWebview = {
        "access_token": os.environ["PAGE_ACCESS_TOKEN"]
    }
    headersWebview = {
        "Content-Type": "application/json"
    }
    dataWebview = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message":{
            "attachment":{
              "type":"template",
              "payload":{
                "template_type":"generic",
                "elements":[
                   {
                    "title":title_arr[0],
                    "image_url":img_arr[0],
                    "subtitle":"",
                    "buttons":[
                        {
                            "type":"web_url",
                            "url":url_arr[0],
                            "title":"consultar"
                          }          
                    ]      
                  },
                  {
                    "title":title_arr[1],
                    "image_url":img_arr[1],
                    "subtitle":"",
                    "buttons":[
                        {
                            "type":"web_url",
                            "url":url_arr[1],
                            "title":"consultar"
                          }             
                    ]      
                  },
                  {
                    "title":title_arr[2],
                    "image_url":img_arr[2],
                    "subtitle":"",
                    "buttons":[
                        {
                            "type":"web_url",
                            "url":url_arr[2],
                            "title":"consultar"
                          }             
                    ]      
                  }
                ]
              }
            }
        }
    })
    wv = requests.post("https://graph.facebook.com/v2.6/me/messages", params=paramsWebview, headers=headersWebview, data=dataWebview)
    if wv.status_code != 200:
        logar(wv.status_code)
        logar(wv.text)

def pass_thread_control(chatter_id):
    passData = json.dumps({
        "recipient": {
            "id": chatter_id
        },
        "target_app_id": 263902037430900,
        "metadata": "-X pass_thread_control X-" 
    })
    passParams = {
        "access_token": os.environ["PAGE_ACCESS_TOKEN"],
    }
    passHeaders = {
        "Content-Type": "application/json"
    }
    hj = requests.post("https://graph.facebook.com/v2.6/me/pass_thread_control", params=passParams, headers=passHeaders, data=passData)
    
    if hj.status_code != 200:
        logar(hj.status_code)
        logar(hj.text)
    else:
        logar("HANDOVER")




if __name__ == '__main__':
    app.run(debug=True)
