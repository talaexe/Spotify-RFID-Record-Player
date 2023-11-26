'''
This is the only file you need to edit. 
1. Edit lines 13-16 with your Spotify details
2. Run spotifyTest.py
3. Run player.py or add song/albums on lines 23 and 31
    (make sure to follow the correct formats)
'''

def init():
    global DEVICE_ID, CLIENT_ID, CLIENT_SECRET
    global SONGS, ALBUMS

    # Edit the Spotify IDs and CLIENT_Secret below
    DEVICE_ID="YOUR_DEVICE_ID"
    CLIENT_ID="YOUR_CLIENT_ID"
    CLIENT_SECRET="YOUR_CLIENT_SECRET"

    # Add songs below if you want one RFID to play one song
    SONGS = {
        # Format:
        #   RFID-CARDVALUE: 'uris_Value'
        865269176938: 'spotify:track:2vSLxBSZoK0eha4AuhZlXV',
        246835529022: 'spotify:track:4PTG3Z6ehGkBFwjybzWkR8',
    }

    # Add albums below if you want one RFID to play an album
    ALBUMS = {
        # Format:
        #   RFID-CARDVALUE: 'context_uri_value',
        865202068078: 'spotify:album:0JGOiO34nwfUdDrD612dOp',
        246777109145: 'spotify:album:6eUW0wxWtzkFdaEFsTJto6',
    }