#!/usr/bin/env python
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

DEVICE_ID="YOUR_DEVICE_ID"
CLIENT_ID="YOUR_CLIENT_ID"
CLIENT_SECRET="YOUR_CLIENT_SECRET"

# Edit here to add one song per RFID tag
SONGS = {
    # Format:
    #   RFID-CARDVALUE: 'uris_Value'
    865269176938: 'spotify:track:2vSLxBSZoK0eha4AuhZlXV',
}

# Edit here to add an album per RFID tag
ALBUMS = {
    # Format:
    #   RFID-CARDVALUE: 'context_uri_value',
    865202068078: 'spotify:album:0JGOiO34nwfUdDrD612dOp',
}

while True:
    try:
        reader=SimpleMFRC522()
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                       client_secret=CLIENT_SECRET,
                                                       redirect_uri="http://localhost:8080",
                                                       scope="user-read-playback-state,user-modify-playback-state"))
        
        # create an infinite while loop that will always be waiting for a new scan
        while True:
            print("Waiting for record scan...")
            id= reader.read()[0]
            print("Card Value is:",id)
            sp.transfer_playback(device_id=DEVICE_ID, force_play=False)
            
            # DONT edit here
            if id in SONGS.keys():

                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=[ SONGS[id] ])
                sleep(2)
                
            elif id in ALBUMS.keys():
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri= ALBUMS[id])
                sleep(2)

    # if there is an error, skip it and try the code again (i.e. timeout issues, no active device error, etc)
    except Exception as e:
        print(e)
        pass

    finally:
        print("Cleaning  up...")
        GPIO.cleanup()
