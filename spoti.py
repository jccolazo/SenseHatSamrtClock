# Ian Annase
# 4/16/18

import os
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError

# Get the username from terminal
username = 'write tour Spotify username'
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username, scope) # add scope
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope) # add scope

# Create our spotify object with permissions
spotifyObject = spotipy.Spotify(auth=token)

# Get current device
try:
    devices = spotifyObject.devices()
    deviceID = devices['devices'][0]['id']
    print(deviceID)
except(IndexError):
    deviceID='vacio'
    print(deviceID)
def is_playing():
    spotifyObject.currently_playing()
def cancion_progreso():
    try:
        track = spotifyObject.current_user_playing_track()
        duracion = track['item']['duration_ms']
        progreso = track['progress_ms']
        resultado=progreso*100/duracion
        resultado=resultado/12.5
        resultado=round(resultado,0)
        return resultado
    except:
        return 0
def cancion_sonando():
    try:
        devices = spotifyObject.devices()
        deviceID = devices['devices'][0]['id']
    except(IndexError):
        deviceID='vacio'
        
    if(deviceID=='vacio' or deviceID!='829e3dc6b6abf108157e8c12dcfa5690e7352ad2'):
        resultado='Cerrado'
    else:
        try:
            track = spotifyObject.current_user_playing_track()
            artist = track['item']['artists'][0]['name']
            track = track['item']['name']
            resultado=(artist+ "-" +track)
        except:
            resultado="Cancion Desconocida"
    return resultado


