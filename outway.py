import os
import requests
from flask import Flask, request
import json
from util import logar


def send_message(message_content, recipient_id):
    send_object = "there seems to be an error"

    logar("OOO - string type - ow_sm - OOO")
    logar(message_content)
    logar(isinstance(message_content, basestring))
    if isinstance(message_content, basestring):
        #                                                     -------------------------------Normal Text
        logar("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_content))
        send_object = { "text": message_content }
   
    else:
     #                                                     -------------------------------Web View
        logar("SEND_WEBVIEW")

        send_object ={
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"generic",
                    "elements": message_content
                }
            }
        }
    #                                                     -------------------------------Sending
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": send_object 
    })
    params = {
        "access_token": os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }

    wv = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if wv.status_code != 200:
        logar(wv.status_code)
        logar(wv.text)

# def senda_message(recipient_id, message_content):

    

#     params = {
#         "access_token": os.environ["PAGE_ACCESS_TOKEN"]
#     }
#     headers = {
#         "Content-Type": "application/json"
#     }
    
#     r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
#     if r.status_code != 200:
#         logar(r.status_code)
#         logar(r.text)