# coding: utf-8
# Last modified: 2014 Jun 24 04:51:38 PM
# xh

import gevent
import signal

def run_forever():
    gevent.sleep(10000)

def close():
    gevent.kill(thread)
    print("closed")

if __name__=='__main__':
    gevent.signal(signal.SIGQUIT, close)
    gevent.signal(signal.SIGTERM, close)
    gevent.signal(signal.SIGINT, close)
    thread = gevent.spawn(run_forever)
    thread.join()
