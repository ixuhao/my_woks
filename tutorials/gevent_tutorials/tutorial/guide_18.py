# coding: utf-8
# Last modified: 2014 Jun 25 01:36:19 PM
# xh

import gevent
from gevent.pool import Pool

pool = Pool(2)

def hello_from(n):
    print('Size of pool %s' % len(pool))

pool.map(hello_from, xrange(3))
