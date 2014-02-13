# coding: utf-8
# xh

import json
import urllib
import urllib2
import pprint
import requests

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
    search_url = API['search']
    params = {
            's': name,
            'limit': 20,
            'csrf_token': ''
    }

    params = urllib.urlencode(params)
    #resp = urllib2.urlopen(search_url, params)
    req = urllib2.Request(search_url, params, HEADERS)
    resp = urllib2.urlopen(req)
    artists = json.loads(resp.read())
    return artists
    #return requests.get(params).json()

s = search('Maroon')
save_json(s, 'Maroon_5.txt')
