
#libraries
import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

username = sys.argv[1]
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

SPOTIPY_REDIRECT_URI

try:
    token=util.prompt_for_user_token(username, scope)
    exept (AttributeError, JSONDecodeError): 
    os.remove(f".cache-{username}")
    token=util.prompt_for_user_token(username, scope)

    spotipy

#for spotipy.oauth2 import SpotifyClientCredentials
#import spotipy
 
#import sys
#import pprint

#import SpotifyClientCredentials
#from spotipy.oauth2 import SpotifyClientCredentials

if len(sys.argv) > 1:
    search_str = sys.argv[1]
else:
    search_str = 'Radiohead'

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
result = sp.search(search_str)
pprint.pprint(result)