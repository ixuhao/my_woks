# coding: utf-8
# Last modified: 2014 Jun 25 09:05:27 AM
# xh

import gevent
from gevent import Timeout

time_to_wait = 5

class TooLong(Exception):
    pass

with Timeout(time_to_wait, TooLong):
    gevent.sleep(10)
