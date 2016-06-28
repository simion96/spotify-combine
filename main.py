import pprint
import sys
import os

import spotipy
import spotipy.util as util
import json




if len(sys.argv) > 1:
    username = sys.argv[1]
    playlist_id = '4upIHtuHeCofqte1XJT1gd'
    playlists = ['1LhvlCvAQnDI5ckCxtdGOK', '5P7aPnGpbJ8Ixq6v11Z9sy', '5kR97nOThA3V2PxKAeBU21', '2YmP0N1kn5KHdz86ZLHkbR']
    #track_ids = ['spotify:track:1xalXygnuN9pA9NejSHfJV', '0PO7fVyPLMShxeh9OKjbWB']
    #track_ids = sys.argv[3:]
else:
    print("Usage: %s username playlist_id track_id ..." % (sys.argv[0],))
    sys.exit()

clientID = os.getenv('SPOTIPY_CLIENT_ID')
clientSecret = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect = os.getenv('SPOTIPY_REDIRECT_URI')
username = '1118158951'
spotifyusername = 'spotifydiscover'

#print clientID
#print clientSecret

scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope, client_id = clientID, client_secret = clientSecret, redirect_uri = redirect)
#
# #doshit
# #username - 1118158951
targetCurrSongs = []
sourceSongs = []
if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False

    mainPlaylist = sp.user_playlist(username, playlist_id, fields='tracks, next')
    items = mainPlaylist['tracks']['items']

    for i in items:
        print json.dumps(i['track']['uri'], indent=2)
        targetCurrSongs.append(i['track']['uri'])

    sp.user_playlist_remove_all_occurrences_of_tracks(user = username, playlist_id = playlist_id, tracks = targetCurrSongs)

    counter = 0
    for playlist in playlists:
        playlist = sp.user_playlist(spotifyusername, playlists[counter], fields='tracks, next')
        playlistItems = playlist['tracks']['items']
        for x in playlistItems:
            sourceSongs.append(x['track']['uri'])
        counter+=1
    print 'source uris: '
    print sourceSongs

    #sp.user_playlist_add_tracks(username, playlist_id, targetCurrSongs)
    sp.user_playlist_add_tracks(username, playlist_id, sourceSongs)

else:
    print("Can't get token for", username)



#spotify:track:1MsyEbEQca1sfC9JnkKnOm
#spotify:track:2ktzBAD5iGVfK1SSE2gFMk


