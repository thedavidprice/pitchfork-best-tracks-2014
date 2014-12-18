from rdio_cred import *
import oauth2 as oauth
import urllib
import urlparse

# create the OAuth consumer credentials
consumer = oauth.Consumer(RDIO_CONSUMER_KEY, RDIO_CONSUMER_SECRET)

# make the initial request for the request token
client = oauth.Client(consumer)
response, content = client.request('http://api.rdio.com/oauth/request_token', 'POST',
                                   urllib.urlencode({'oauth_callback':'oob'}))
parsed_content = dict(urlparse.parse_qsl(content))
request_token = oauth.Token(parsed_content['oauth_token'], parsed_content['oauth_token_secret'])

print "request token:", request_token

# # ask the user to authorize this application
print 'Authorize this app at: %s?oauth_token=%s&grant_type=password&username=%s&password=%s' \
      % (parsed_content['login_url'], parsed_content['oauth_token'], USERNAME, PASSWORD)
oauth_verifier = raw_input('Enter the PIN / OAuth verifier: ').strip()
# associate the verifier with the request token
request_token.set_verifier(oauth_verifier)

# # upgrade the request token to an access token
client = oauth.Client(consumer, request_token)
response, content = client.request('http://api.rdio.com/oauth/access_token', 'POST')
parsed_content = dict(urlparse.parse_qsl(content))
access_token = oauth.Token(parsed_content['oauth_token'], parsed_content['oauth_token_secret'])

## make an authenticated API call
client = oauth.Client(consumer, access_token)
response = client.request('http://api.rdio.com/1/', 'POST', urllib.urlencode({'method': 'currentUser'}))
print response[1]

print "Access Token FTW! Pro Tip --> Save this bad boy:)", access_token