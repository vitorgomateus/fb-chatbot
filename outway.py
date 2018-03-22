import os
import requests
from flask import Flask, request
import json
from util import logar

def send_webview(title_arr, img_arr, url_arr, recipient_id):
    logar("SEND_WEBVIEW")
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

def senda_message(recipient_id, message_text):

    logar("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

    params = {
        "access_token": os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        logar(r.status_code)
        logar(r.text)