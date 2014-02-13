# coding: utf-8
# xh
# according to NeteaseCloudMusic.py @author: Yang Junyong <yanunon@gmail.com>

import json
import urllib
import urllib2
import pprint

# API
API = {
  'search': 'http://music.163.com/api/search/suggest/web',
  'album': 'http://music.163.com/api/album/',
  'detail': 'http://music.163.com/api/song/detail',
  'playlist': 'http://music.163.com/api/playlist/detail',
  'dj': 'http://music.163.com/api/dj/program/detail'
}

HEADERS = {
  #'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
  "User-Agent":  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36",
  'Referer': 'http://music.163.com/'
}

def save_json(j, dst):
    with open(dst, 'w') as f:
        pprint.pprint(j, f)

def search(name):
    """ return songs, artists, albums, playlists, etc"""
    search_url = API['search']
    params = {
            's': name,
            'limit': 20,
            'csrf_token': ''
    }

    params = urllib.urlencode(params)
    req = urllib2.Request(search_url, params, HEADERS)
    resp = urllib2.urlopen(req)
    artists = json.loads(resp.read())
    return artists

def get_song_by_id(sid):
    """ return song detail """
    query_url = API['detail']
    params = {
            'id': sid,
            'ids': '[' + sid + ']',
            'csrf_token': ''
            }
    params = urllib.urlencode(params)
    req = urllib2.Request(query_url, params, HEADERS)
    resp = urllib2.urlopen(req)
    return json.loads(resp.read())

def download_mp3(url, name):
    m = urllib2.urlopen(url)
    with open(name+'.mp3', 'wb') as f:
        f.write(m.read())

# search demo
#s = search('Maroon 5')
#save_json(s, 'Maroon_5.txt')
#print s['result']['artists'][0]
#s = search('Radioactive')
#save_json(s, 'search_results.txt')
#for song in s['result']['songs']:
#    print song['name']
#    print song['artists'][0]['name']
#    print song['id']

# download 外面的世界 莫文蔚 276904
#s = get_song_by_id('276904')
s = get_song_by_id('67143')
#save_json(s, 'songs_results.txt')
song = s['songs'][0]
song_name = song['name']
song_artists = song['artists']
artist_name = ''.join(i['name'] for i in song_artists)
mp3_name = song_name + '_' + artist_name
print mp3_name
mp3_url = song['mp3Url']
print mp3_url
download_mp3(mp3_url, mp3_name)
