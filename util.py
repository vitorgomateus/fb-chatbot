
import sys
import json
from datetime
from util import logar

def logar(msg, *args, **kwargs):  # simple wrapper for logging to stdout on heroku 

                                ### This function is giving me errors, but it's not clear what the problem is.
                                ### I always call it with only one parameter, a string or a 'dict', 
                                ###     and usually there is no problem.
                                ### but when I call it to log the http response is when errors show up.
    try:
        if type(msg) is dict:
            msg = json.dumps(msg)
        #else:
            #msg = unicode(msg).format(*args, **kwargs) ### If I comment this line, no error shows up
            #msg=msg
        print u"{}: {}".format(datetime.now(), msg)
    except UnicodeEncodeError:
        pass  # squash logging errors in case of non-ascii text
    sys.stdout.flush()

