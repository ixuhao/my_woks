# coding: utf-8
# Last modified: 2014 Jun 25 09:03:24 AM
# xh

import gevent
from gevent import Timeout

seconds = 5

timeout = Timeout(seconds)
timeout.start()

def wait():
    gevent.sleep(10)

try:
    gevent.spawn(wait).join()
except Timeout:
    print('Could not complete')
