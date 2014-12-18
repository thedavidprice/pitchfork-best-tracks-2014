#####
# once we have all the credentials stored, use this simple test to confirm they're valid
#####

import urllib
import oauth2 as oauth
from rdio_cred import *

# create the OAuth consumer credentials
consumer = oauth.Consumer(RDIO_CONSUMER_KEY, RDIO_CONSUMER_SECRET)

# and the user oauth tokens
access_token = oauth.Token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

## make an authenticated API call
client = oauth.Client(consumer, access_token)
response = client.request('http://api.rdio.com/1/', 'POST', urllib.urlencode({'method': 'currentUser'}))
print response[1]
