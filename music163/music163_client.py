# coding: utf-8
# xh
# https://github.com/sneezry/music.163.com/blob/master/js/api.js
# also according to NeteaseCloudMusic.py @author: Yang Junyong <yanunon@gmail.com>

import json
import urllib
import urllib2
import re
import time

API = {
        'album': 'http://music.163.com/album?id=',
        'detail': 'http://music.163.com/api/song/detail',
        }

HEADERS = {
  #'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
  "User-Agent":  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36",
  'Referer': 'http://music.163.com/'
}

def download_mp3(url, name):
    m = urllib2.urlopen(url)
    with open(name+'.mp3', 'wb') as f:
        f.write(m.read())

def get_song_by_id(sid):
    query_url = API['detail']
    params = {
            'id': sid,
            'ids': '[' + sid + ']',
            'csrf_token': ''
            }
    params = urllib.urlencode(params)
    req = urllib2.Request(query_url, params, HEADERS)
    resp = urllib2.urlopen(req)
    song_json = json.loads(resp.read())
    if song_json:
        song = song_json['songs'][0]
        song_name = song['name']
        song_artists = song['artists']
        artist_name = ''.join(i['name'] for i in song_artists)
        mp3_name = song_name + '_' + artist_name
        print mp3_name
        mp3_url = song['mp3Url']
        print mp3_url
        download_mp3(mp3_url, mp3_name)
    else:
        return None

def get_alumn_by_id(aid):
    req = urllib2.Request(API['album']+aid)
    resp = urllib2.urlopen(req).read()

    song_reg = 'song\?id=(\d+)'
    match = re.findall(song_reg, resp)
    print match
    for m in match:
        get_song_by_id(m)
        time.sleep(10)

if __name__ == '__main__':
    #song_id = '276904'
    #get_song_by_id(song_id)

    album_id = '2461019' #http://music.163.com/album?id=2461019
    get_alumn_by_id(album_id)
