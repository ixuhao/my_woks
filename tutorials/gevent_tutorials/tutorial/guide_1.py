# coding: utf-8
# Last modified: 2014 Jun 24 02:52:56 PM
# xh

import gevent

def foo():
    print("Running in foo")
    gevent.sleep(0)
    print("Explicit context switch to foo again")

def bar():
    print("Explicit context to bar")
    gevent.sleep(0)
    print("Implicit context switch back to bar")


gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
    ])
