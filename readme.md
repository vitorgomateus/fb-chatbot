# Um Chatbot Experimental

	x-> handover protocol aplicado
	x-> faz request a informação da REST API do wooCommerce
	x-> consegue enviar webviews com sucesso

----

-to get events from manned messages of my page, I apparently need to subscribe the bot to: messages; messaging_handover; message_echoes; standby

-https://pypi.python.org/pypi/WooCommerce
	http://woocommerce.github.io/woocommerce-rest-api-docs/?python#list-all-products

O - BD
https://pypi.python.org/pypi/python-firebase/1.2
https://console.firebase.google.com/project/bottesting-testbotting/overview
O - Wordpress REST API para armazenar dados dos utilizadores no facebook? - no good keeping people's data :/

-< https://developers.facebook.com/docs/messenger-platform/send-messages/quick-replies

O - fazer esperar um bocadinho para dar tempo a uma pessoa de pegar na conversa?

O - bot reage a várias mensagens em simultaneo :S

X - tags ou atributes para filtrar linguas
	- Wordpress API?		https://pypi.python.org/pypi/wordpress-api/1.2.6	
	O WC tem os post_type=product available para a rest api? - http://v2.wp-api.org/extending/custom-content-types/
	É mesmo preciso usar o WC_API pyPa para conseguir obter produtos? - https://nology.de/wordpress-api-v2-with-polylang-and-acf.html
		ESTE FUNCIONOU :D
	Ou posso simplesmente usar o Requests pyPa?
	x - Não tenho controlo sobre que lingua escolhe, assumo que escolha a lingua do mesmo modo que o site o faz.


O - Interpretar texto
	-regex?


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


# Facebook Messenger Bot
This is a simple python template that uses Flask to build a webhook for Facebook's Messenger Bot API.

Read more in my [tutorial that uses this repository](https://blog.hartleybrody.com/fb-messenger-bot/).

*New:* [Check out my Facebook Messenger Bot Course](https://facebook-messenger-bot.teachable.com/p/facebook-messenger-bot/). It walks you through the process of getting this bot hosted on heroku step-by-step, and also unlocks all the content that's hidden in this repo's branches.

## "Callback verification failed"

![Facebook Error](https://cloud.githubusercontent.com/assets/18402893/21538944/f96fcd1e-cdc7-11e6-83ee-a866190d9080.png)

The #1 error that gets reported in issues is that facebook returns an error message (like above) when trying to add the heroku endpoint to your facebook chat application.

Our flask application intentionally returns a 403 Forbidden error if the token that facebook sends doesn't match the token you set using the heroku configuration variables.

If you're getting this error, it likely means that you didn't set your heroku config values properly. Run `heroku config` from the command line within your application and verify that there's a key called `VERIFY_TOKEN` that has been set, and that it's set to the same value as what you've typed into the window on facebook.