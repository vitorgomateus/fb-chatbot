import os
import requests
from flask import Flask, request
import json
from util import logar


def send_message(message_content, recipient_id):
    send_object = "there seems to be an error"

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


def send_quick_reply( text_str, set_num, recipient_id):
    #https://cdn3.iconfinder.com/data/icons/diagram_v2/PNG/32x32/diagram_v2-23.png
    #https://cdn3.iconfinder.com/data/icons/diagram_v2/PNG/32x32/diagram_v2-27.png
    #https://cdn3.iconfinder.com/data/icons/diagram_v2/PNG/32x32/diagram_v2-10.png
    #https://cdn1.iconfinder.com/data/icons/military-filled/64/army-09-48.png
    qr= [
      {
        "content_type":"text",
        "title":"Search",
        "payload":"User Hit Search",
        "image_url":"https://cdn3.iconfinder.com/data/icons/diagram_v2/PNG/32x32/diagram_v2-10.png"
      },
      {
        "content_type":"location",
        "title":"where do I send te nukes?",
        "image_url":"https://cdn1.iconfinder.com/data/icons/military-filled/64/army-09-48.png"
      },
      {
          "content_type":"text",
          "title":"hit me please!!!",
          "payload":"QR_COF",
          "image_url":"https://cdn3.iconfinder.com/data/icons/diagram_v2/PNG/32x32/diagram_v2-23.png"
      }
    ]

    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": text_str,
            "quick_replies":qr
        }
    })
    params = {
        "access_token": os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }

    rq = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if rq.status_code != 200:
        logar(rq.status_code)
        logar(rq.text)

def get_user_name(user_id):

#"https://graph.facebook.com/v2.6/<PSID>?fields=first_name,last_name,profile_pic&access_token=<PAGE_ACCESS_TOKEN>"
    params = {
        "access_token": os.environ["PAGE_ACCESS_TOKEN"],
        "fields":"first_name"
    }
    headers = {
        "Content-Type": "application/json"
    }
    
    u = requests.get("https://graph.facebook.com/v2.6/{userPSID}".format(userPSID=user_id), params=params, headers=headers)
    if u.status_code != 200:
        logar(u.status_code)
        logar(u.text)

    user=u.json()
    logar("OOO - user name")
    logar(user["first_name"])
    return user["first_name"]
        