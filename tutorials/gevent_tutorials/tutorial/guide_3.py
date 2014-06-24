# coding: utf-8
# Last modified: 2014 Jun 24 03:36:50 PM
# xh

import gevent
import random


def task(pid):
    #gevent.sleep(random.randint(0, 2)*0.001)
    t = random.randint(0, 5)
    gevent.sleep(t)
    print("Task %s Done.: %d" % (pid, t))

def synchronous():
    for i in range(1, 10):
        task(i)


def asynchronous():
    threads = [gevent.spawn(task, i) for i in xrange(10)]
    gevent.joinall(threads)

print('Synchronous')
synchronous()

print('Asynchronous')
asynchronous()
