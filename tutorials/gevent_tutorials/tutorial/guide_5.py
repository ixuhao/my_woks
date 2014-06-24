# coding: utf-8
# Last modified: 2014 Jun 24 04:20:05 PM
# xh

import gevent
from gevent import Greenlet

class MyGreenlet(Greenlet):

    def __init__(self, message, n):
        Greenlet.__init__(self)
        self.message = message
        self.n = n

    def _run(self):
        print(self.message)
        gevent.sleep(self.n)

g = MyGreenlet('Hi there!', 3)
g.start()
g.join()
