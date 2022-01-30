#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep


while True:
    try:
        reader=SimpleMFRC522()
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="8a78f3a342f743f38a0de0ebcca824b6",
                                                       client_secret="3af83c6b714948bf867e978d1a4f3a3c",
                                                       redirect_uri="http://localhost:8080",
                                                       scope="user-read-playback-state,user-modify-playback-state"))

        while True:
            id= reader.read()[0]
            print(id)
            sp.transfer_playback(device_id="98bb0735e28656bac098d927d410c3138a4b5bca", force_play=False)
            if (id==554295573797):
                sp.start_playback(device_id="98bb0735e28656bac098d927d410c3138a4b5bca", uris=['spotify:track:2vSLxBSZoK0eha4AuhZlXV'])
                sleep(2)
            elif (id==573757500451):
                sp.start_playback(device_id="98bb0735e28656bac098d927d410c3138a4b5bca", uris=['spotify:track:4tsQ8uAYsZUagN4CiJRylI'])
                sleep(2)
            elif (id==765982546927):
                sp.start_playback(device_id="98bb0735e28656bac098d927d410c3138a4b5bca", uris=['spotify:track:5QO79kh1waicV47BqGRL3g'])
                sleep(2)
            elif (id==739499588896):
                sp.start_playback(device_id="98bb0735e28656bac098d927d410c3138a4b5bca", uris=['spotify:track:4YIP6Fo4UXUimnsdYKLqXy'])
                sleep(2)
            # lady of namek
            elif (id==246777109145):
                sp.start_playback(device_id="98bb0735e28656bac098d927d410c3138a4b5bca", uris=['spotify:track:6btIpLff2jE56h2N40smAj'])
                sleep(2)
            # happier than ever
            elif (id==40618678953):
                sp.start_playback(device_id="98bb0735e28656bac098d927d410c3138a4b5bca", context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                sleep(2)
            #enchanted
            elif (id==933955099256):
                sp.start_playback(device_id="98bb0735e28656bac098d927d410c3138a4b5bca", uris=['spotify:track:10eBRyImhfqVvkiVEGf0N0'])
                sleep(2)
            # blsxt no love lost
            elif (id==865202068078):
                sp.start_playback(device_id="98bb0735e28656bac098d927d410c3138a4b5bca", context_uri='spotify:album:7AwrgenNcTAJlJF3pKL0Qr')
                sleep(2)
            #r&b mix
            elif (id==932982020662):
                sp.start_playback(device_id="98bb0735e28656bac098d927d410c3138a4b5bca", context_uri='spotify:playlist:37i9dQZF1EQoqCH7BwIYb7')
                sleep(2)
            # daily mix
            elif (id==726823590470):
                sp.start_playback(device_id="98bb0735e28656bac098d927d410c3138a4b5bca", context_uri='spotify:playlist:37i9dQZF1E35YDGo2i2MEc')
                sleep(2)
            # justice
            elif (id==865269176938):
                sp.start_playback(device_id="98bb0735e28656bac098d927d410c3138a4b5bca", context_uri='spotify:album:5dGWwsZ9iB2Xc3UKR0gif2')
                sleep(2)
            # after hrs
            elif (id==865235622504):
                sp.start_playback(device_id="98bb0735e28656bac098d927d410c3138a4b5bca", context_uri='spotify:album:4yP0hdKOZPNshxUOjY0cZj')
                sleep(2)
            # starboy
            elif (id==796482591262):
                sp.start_playback(device_id="98bb0735e28656bac098d927d410c3138a4b5bca", context_uri='spotify:album:2ODvWsOgouMbaA5xf0RkJe')
                sleep(2)
            #parachutes
            elif (id==1071343721053):
                sp.start_playback(device_id="98bb0735e28656bac098d927d410c3138a4b5bca", context_uri='spotify:album:6ZG5lRT77aJ3btmArcykra')
                sleep(2)
            #channel orange
            elif (id==314506730150):
                sp.start_playback(device_id="98bb0735e28656bac098d927d410c3138a4b5bca", context_uri='spotify:album:392p3shh2jkxUxY2VHvlH8')
                sleep(2)
            #pop mix                
            elif (id==520665160342):
                sp.start_playback(device_id="98bb0735e28656bac098d927d410c3138a4b5bca", context_uri='spotify:playlist:37i9dQZF1EQncLwOalG3K7')
                sleep(2)
    except:
        pass

    finally:
        print("Cleaning  up...")
        GPIO.cleanup()


