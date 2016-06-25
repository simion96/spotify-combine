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
    #for track in mainPlaylist['items']:
    #    print track['']
    tracks =  mainPlaylist['tracks']
    #tracks =  mainPlaylist


    items =  tracks['items']
    print json.dumps(items, indent=2)

    for i in items:
        print json.dumps(i['track']['uri'], indent=2)
        targetCurrSongs.append(i['track']['uri'])
    print "content of list is: "
    print targetCurrSongs[:]
    #print items
    #pprint.pprint(tracks)
    #show_tracks(mainPlaylist)
    #print mainPlaylist['is_local']
    #print mainPlaylist['items']['track']['id']

    #results = sp.user_playlists(username)

    #for song in results[]
    #pprint.pprint(results)

    #playlists = sp.user_playlists(username)
    #for playlist in playlists['items']:
    #    print playlist

else:
    print("Can't get token for", username)


def show_tracks(tracks):
 for i, item in enumerate(tracks['items']):
     track = item['track']
     print "   %d %32.32s %s" % (i, track['artists'][0]['name'],
         track['name'])


