import pprint
import sys
import os

import spotipy
import spotipy.util as util
import json




if len(sys.argv) > 1:
    username = sys.argv[1]
    #playlist_id = 'spotify:user:1118158951:playlist:40YEYqJ3SOytr5ll3FNXKd'
    playlist_id = '40YEYqJ3SOytr5ll3FNXKd'
    track_ids = ['spotify:track:1xalXygnuN9pA9NejSHfJV', '0PO7fVyPLMShxeh9OKjbWB']
    #track_ids = ['1xalXygnuN9pA9NejSHfJV', '0PO7fVyPLMShxeh9OKjbWB']
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
    #track1 = sys.argv[2]
    #print "track to request: " + track1

    #https://open.spotify.com/track/1xalXygnuN9pA9NejSHfJV

    print "track ids[0] is " + track_ids[0]
    results = sp.user_playlist_remove_all_occurrences_of_tracks(user = username, playlist_id = playlist_id, tracks = targetCurrSongs)
else:
    print("Can't get token for", username)


