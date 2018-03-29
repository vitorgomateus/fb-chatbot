import os
import requests
# Persistent menu:
# 	1- About Us:
# 		1.1 - What do we do?
# 		1.2 - What is a Friend?
# 		1.3 - Where do we have programs?
# 		1.4 - visit website:
# 	2- How to's:
# 		2.1 - How to join as a Friend?
# 		2.2 - How to book a program?
# 	3- Things I can do:
# 		3.1 - Get programs
# 		3.2 - Pass to a human
def set_persistent_menu():
	data = json.dumps({
	  "persistent_menu":[
	    {
	      "locale":"default",
	      "composer_input_disabled": true,
	      "call_to_actions":[
	        {
	          "title":"About Us",
	          "type":"nested",
	          "call_to_actions":[
	            {
	              "title":"What is a Friend?",
	              "type":"postback",
	              "payload":"<PM_1.1>"
	            },{
	              "title":"Where do we have programs?",
	              "type":"postback",
	              "payload":"<PM_1.2>"
	            },{
	              "title":"What do we do?",
	              "type":"postback",
	              "payload":"<PM_1.3>"
	            },
	            {
	              "type":"web_url",
	              "title":"visit",
	              "url":"https://www.myfriendsinportugal.com"
	            }
	          ]
	        },{
	          "title":"How to's:",
	          "type":"nested",
	          "call_to_actions":[
	            {
	              "title":"How to join as a Friend?",
	              "type":"postback",
	              "payload":"<PM_2.1>"
	            },{
	              "title":"How to book a program?",
	              "type":"postback",
	              "payload":"<PM_2.2>"
	            }
	          ]
	        },{
	          "title":"Things I can do:",
	          "type":"nested",
	          "call_to_actions":[
	            {
	              "title":"Get the latest programs",
	              "type":"postback",
	              "payload":"<PM_3.1>"
	            },{
	              "title":"Pass to a human...",
	              "type":"postback",
	              "payload":"<PM_3.2>"
	            }
	          ]
	        }
	      ]
	    }
	  ]
	})
    params = {
        "access_token": os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }

    mp = requests.post("https://graph.facebook.com/v2.6/me/messenger_profile", params=params, headers=headers, data=data)
    if mp.status_code != 200:
        logar(mp.status_code)
        logar(mp.text)


