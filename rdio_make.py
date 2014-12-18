from rdio_cred import *
import csv
from rdio import Rdio

def create_playlist(key_string):
	rdio.call('createPlaylist', {'name': PLAYLIST_NAME, 'description': PLAYLIST_DESCRIPTION, 'tracks': key_string})

# initiate rdio object
rdio = Rdio((RDIO_CONSUMER_KEY, RDIO_CONSUMER_SECRET), (OAUTH_TOKEN, OAUTH_TOKEN_SECRET))

csv_tracks = []
f = open('track_list.csv', 'rU')
reader = csv.reader(f)
for row in reader:
    csv_tracks.append({'artist': row[0], 'title': row[1]})
f.close()

# first build a list of all tracks found that can be streamed
key_list = []
for track in csv_tracks:
	query = track['artist'] + ' ' + track['title']
	search = rdio.call('search', {'query': query, 'types': 'Track'})
	if search['result']['number_results'] > 0:
		if search['result']['results'][0]['canStream']:
			# add_to_playlist(search['result']['results'][0]['key'])
			key_list.append(search['result']['results'][0]['key'])
			print "Adding %s by %s to the playlist" % (track['title'], track['artist'])
		else:
			print "NO STREAM: %s by %s" % (track['title'], track['artist'])
	else:
		print "NOT AVAILABLE %s by %s to the playlist" % (track['title'], track['artist'])

# convert list to string for use in rdio createplaylist call
key_list_string = ','.join(map(str, key_list))

# do it, finally
create_playlist(key_list_string)

# feel good about small wins in life
print "\n", "=" * 20
print "You WIN the GAME!!"