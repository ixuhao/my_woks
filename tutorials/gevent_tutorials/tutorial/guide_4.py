# coding: utf-8
# Last modified: 2014 Jun 24 04:14:17 PM
# xh

import gevent.monkey
gevent.monkey.patch_socket()

import gevent
import urllib2
import json

def fetch(pid):
    response = urllib2.urlopen("http://time.jsontest.com/")
    result = response.read()
    json_result = json.loads(result)
    datetime = ' '.join([json_result['date'], json_result['time']])

    print("Process %s: %s" % (pid, datetime))
    return datetime

def synchronous():
    for i in range(1, 10):
        fetch(i)

def asynchronous():
    threads = []
    for i in range(1, 10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)

print("Synchronous")
#synchronous()

print("Asynchronous")
asynchronous()
