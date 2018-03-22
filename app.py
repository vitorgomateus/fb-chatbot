import os
#import sys
import json
#from datetime import datetime

import requests
from flask import Flask, request

from getway import get_send_products
from outway import senda_message, send_webview
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
    time.sleep(500) 

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
                               send_message(sender_id, "BOT :D")
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
