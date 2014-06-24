# coding: utf-8
# Last modified: 2014 Jun 24 03:25:04 PM
# xh

import time
import gevent
from gevent import select

start = time.time()
tic = lambda: 'at %1.1f seconds.' % (time.time() - start)

def gr1():
    print("Started Polling1: %s" % tic())
    select.select([], [], [], 2)
    print('Ended Polling1: %s' % tic())

def gr2():
    print("Started Polling2: %s" % tic())
    select.select([], [], [], 2)
    print('Ended Polling2: %s' % tic())

def gr3():
    print("Hey lets do some stuff while the greenlets poll: %s" % tic())
    gevent.sleep(1)

gevent.joinall([
    gevent.spawn(gr1),
    gevent.spawn(gr2),
    gevent.spawn(gr3),
    ])
