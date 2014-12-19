#Pitchfork Best Tracks of 2014: Rdio Playlist
==========================
_Original List Here:_  
http://pitchfork.com/features/staff-lists/9555-the-100-best-tracks-of-2014

_Rdio Playlist Here:_  
http://rd.io/x/QVFJ8zPkeEw/

Simple python script to generate an Rdio playlist from a www.import.io data scrape of Pitchfork's website.

##Setup
1. You'll need an API Key. Sign up for Rdio Mashery via the "Manage Apps" link here: http://www.rdio.com/developers/
2. Developer Documentation here: http://www.rdio.com/developers/docs/
3. You'll need this: https://github.com/rdio/rdio-simple/tree/master/python
4. And this, too: https://github.com/seatgeek/fuzzywuzzy

##Oauth Authentication
1. create a file rdio_cred.py (use rdio_cred_TEMPLATE.py) with the following variables. You should have the consumer key and secret from the Rdio Mashery. Use your username and password. You won't have OAUTH yet:  
`RDIO_CONSUMER_KEY = ' '  
RDIO_CONSUMER_SECRET = ' '  
USERNAME = ' '  
PASSWORD = ' '  
OAUTH_TOKEN_SECRET = ' '  
OAUTH_TOKEN = ' '`
2. Run the rdio_api_auth.py script from console. Follow the instructions to Authenticate including copy/paste url into browser to get the pin.
3. **Save** the OAUTH token and secret that print out. Paste them into rdio_cred.py

##Finally, Create the Playlist
Once you're ready to rock (pun intended), just run `rdio_make.py`

Enjoy!

##TO DO
- [ ] Needs fuzzy search and/or better matching  
- [ ] Output list of missing tracks  
- [ ] Cron inspector to 1) remove tracks no longer available and/or 2) add tracks now available  (?) 
- [ ] Db (?) 
- [ ] Option to go through auth each time or save use tokens (?)  

