import os
import requests
from flask import Flask, request
import json
from util import logar

#                message_text = if isWebView ? 0 : text
def send_message(message_text, recipient_id, title_arr, img_arr, url_arr):
    send_object = "there seems to be an error"
    logar("title_arr")
    logar(title_arr[1])
    logar(title_arr)

    if(message_text==0):
    #                                                     -------------------------------Web View
        logar("SEND_WEBVIEW")

        element = []
        #if(!(len(title_arr)==len(img_arr)==len(url_arr))):
        #    logar("length of arrays in outway.py->send_webview is in discord")
        for i in title_arr:
            element = {
                        "title":title_arr[i],
                        "image_url":img_arr[i],
                        "subtitle":"",
                        "buttons":[
                            {
                                "type":"web_url",
                                "url":url_arr[i],
                                "title":"Read More"
                              }          
                        ]      
                      }
            logar("element{num}".format(num=i))
            logar(element)
            arr_elements += element;

            logar("arr_elements")
            logar(arr_elements)

        send_object ={
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"generic",
                    "elements": arr_elements
                }
            }
        }
            

    else:
    #                                                     -------------------------------Normal Text
        logar("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))
        send_object = { "text": message_text }

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

# def senda_message(recipient_id, message_text):

    

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