import urllib
import json
import logging

LASTFM_API_URL = 'http://ws.audioscrobbler.com/2.0'

#Get an API Account at http://www.last.fm/api/accounts
API_KEY = '2993c6e15c91a2890c2f11fa95673067'

def get_recent_tracks(user):

    values = {'url':LASTFM_API_URL,'method':'user.getrecenttracks','user': user,'api_key': API_KEY}

    url = "%(url)s/?method=%(method)s&user=%(user)s&api_key=%(api_key)s&format=json" % values

    try:
        response = urllib.urlopen(url)
        resp = json.loads(response.read())
    except Exception, e:
        logging.warning('lastfm') 
        return None

    recent_tracks = resp['recenttracks']
    raw_tracks = recent_tracks['track']
    tracks = []
    for raw_track in raw_tracks:
        try:
           imgsrc = raw_track['image'][0]["#text"]
           if imgsrc == "":
              imgsrc = "http://cdn.last.fm/flatness/catalogue/noimage/2/default_artist_small.png"
           track = {
                   'name': raw_track['name'],
                   'artist': raw_track['artist']['#text'],
                   'url': raw_track['url'],
                   'image_url': imgsrc
                   }
           tracks.append(track)
        except Exception, e:
            logging.warning('last.fm');

    return tracks

tracks = get_recent_tracks('yelf')

print tracks[0]['artist'] + ' | ' + tracks[0]['name']