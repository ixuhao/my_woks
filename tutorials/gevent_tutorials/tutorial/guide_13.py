# coding: utf-8
# Last modified: 2014 Jun 25 09:36:03 AM
# xh

import gevent
from gevent.event import AsyncResult
a = AsyncResult()

def setter():
    gevent.sleep(3)
    a.set('Hello')

def waiter():
    print(a.get())

gevent.joinall([
    gevent.spawn(setter),
    gevent.spawn(waiter),
    ])
