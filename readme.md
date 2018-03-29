# Um Chatbot Experimental

	x-> handover protocol aplicado
	x-> faz request a informação da REST API do wooCommerce
	x-> consegue enviar webviews com sucesso
	o-> quick replies
	o-> writting smtg
	o-> interpretar texto
	o-> guardar informação

----

-to get events from manned messages of my page, I apparently need to subscribe the bot to: messages; messaging_handover; message_echoes; standby

-https://pypi.python.org/pypi/WooCommerce
	http://woocommerce.github.io/woocommerce-rest-api-docs/?python#list-all-products

O - BD
https://pypi.python.org/pypi/python-firebase/1.2	
https://console.firebase.google.com/project/bottesting-testbotting/overview
O - Wordpress REST API para armazenar dados dos utilizadores no facebook? - no good keeping people's data :/

-< https://developers.facebook.com/docs/messenger-platform/send-messages/quick-replies
-< https://blog.messengerdevelopers.com/using-the-webview-to-create-richer-bot-to-user-interactions-ed8a789523c6
-< https://stanfy.com/blog/facebook-messenger-bots-interactions/

X - tags ou atributes para filtrar linguas
	- Wordpress API?		https://pypi.python.org/pypi/wordpress-api/1.2.6	
	O WC tem os post_type=product available para a rest api? - http://v2.wp-api.org/extending/custom-content-types/
	É mesmo preciso usar o WC_API pyPa para conseguir obter produtos? - https://nology.de/wordpress-api-v2-with-polylang-and-acf.html
		ESTE FUNCIONOU :D
	Ou posso simplesmente usar o Requests pyPa?
	x - Não tenho controlo sobre que lingua escolhe, assumo que escolha a lingua do mesmo modo que o site o faz.

O - fazer esperar um bocadinho para dar tempo a uma pessoa de pegar na conversa?


O - Interpretar texto
	-regex?

O - bot reage a várias mensagens em simultaneo :S


O - usar google pre-filled link para registar friends através do messenger - REQUIRES DB
	"https://docs.google.com/forms/d/e/1FAIpQLSd3JFWwtKtPgZk1JjfQ1ygUcBBBAl3xGVlyqBKTnIn36KShyA/viewform?usp=pp_url&entry.539221635=your+name&entry.560854717=2018-05-21&entry.122999599=6665556565&entry.52689714=5454dfdfd54&entry.686443584=gfgj&entry.693683744=hjdghjfgh&entry.1380086835=fhgjfhgj&entry.816296692=fghjfghjfgh&entry.1556765854=Inclui+lugares+a+visitar?&entry.426540354=Adultos&entry.400601593=1+hora&entry.235041046=ghjfhj&entry.1237964408=fghjfgh&entry.1573059110=fhgjfghj&entry.488807207=Portugu%C3%AAs&entry.488807207=Espanhol"

-> It's going good and looking alive ;)

heroku apps
heroku create
heroku open
heroku logs -t
-
git add&commit$push
git push heroku master
heroku open
heroku config:add VERIFY_TOKEN=your_verification_token_here

--------------------------
iterate through dicts with dicts:
def myprint(d):
  for k, v in d.items():
    if isinstance(v, dict):
      myprint(v)
    else:
      print("{0} : {1}".format(k, v))


# About Conversations flowgram

Persistent menu:
	1- About Us:
		1.1 - What do we do?
		1.2 - What is a Friend?
		1.3 - Where do we have programs?
		1.4 - visit website:
	2- How to's:
		2.1 - How to be a Friend?
		2.2 - how to book a program?
	3- Things I can do:
		3.1 - Get programs
		3.2 - Pass to a human
		3.3 - Get programs by category:	---		X
		3.4 - Book a programs 			---		X
		3.5 - Apply to be a friends 	---		X


Client retention flow:
-Awereness
-Cosideration
-Purchase
-Retention
-Advocacy



# Facebook Messenger Bot
This is a simple python template that uses Flask to build a webhook for Facebook's Messenger Bot API.

Read more in my [tutorial that uses this repository](https://blog.hartleybrody.com/fb-messenger-bot/).

*New:* [Check out my Facebook Messenger Bot Course](https://facebook-messenger-bot.teachable.com/p/facebook-messenger-bot/). It walks you through the process of getting this bot hosted on heroku step-by-step, and also unlocks all the content that's hidden in this repo's branches.

## "Callback verification failed"

![Facebook Error](https://cloud.githubusercontent.com/assets/18402893/21538944/f96fcd1e-cdc7-11e6-83ee-a866190d9080.png)

The #1 error that gets reported in issues is that facebook returns an error message (like above) when trying to add the heroku endpoint to your facebook chat application.

Our flask application intentionally returns a 403 Forbidden error if the token that facebook sends doesn't match the token you set using the heroku configuration variables.

If you're getting this error, it likely means that you didn't set your heroku config values properly. Run `heroku config` from the command line within your application and verify that there's a key called `VERIFY_TOKEN` that has been set, and that it's set to the same value as what you've typed into the window on facebook.