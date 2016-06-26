import pprint
import sys
import os

import spotipy
import spotipy.util as util
import json




if len(sys.argv) > 1:
    username = sys.argv[1]
    playlist_id = '40YEYqJ3SOytr5ll3FNXKd'
    track_ids = ['5QCTcIMAfMuTGDvttwDBv1', '0PO7fVyPLMShxeh9OKjbWB']
    #playlist_id = sys.argv[2]
    #track_ids = sys.argv[3:]
else:
    print("Usage: %s username playlist_id track_id ..." % (sys.argv[0],))
    sys.exit()

clientID = os.getenv('SPOTIPY_CLIENT_ID')
clientSecret = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect = os.getenv('SPOTIPY_REDIRECT_URI')
username = '1118158951'

#print clientID
#print clientSecret

scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope, client_id = clientID, client_secret = clientSecret, redirect_uri = redirect)
#
# #doshit
# #username - 1118158951
targetCurrSongs = []
if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False

    mainPlaylist = sp.user_playlist(username, playlist_id, fields='tracks, next')
    items = mainPlaylist['tracks']['items']
    print json.dumps(items, indent=2)

    for i in items:
        #print json.dumps(i['track']['uri'], indent=2)
        targetCurrSongs.append(i['track']['uri'])
    print "content of list is: "
    print targetCurrSongs[:]

    print targetCurrSongs[1]
    track1 = sys.argv[2]
    print "track to request: " + track1
    results = sp.user_playlist_remove_all_occurrences_of_tracks(username, playlist_id, track1)
else:
    print("Can't get token for", username)


