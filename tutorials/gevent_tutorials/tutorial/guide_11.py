# coding: utf-8
# Last modified: 2014 Jun 25 09:19:23 AM
# xh

import socket
print(socket.socket)

print("After monkey path")
from gevent import monkey
monkey.patch_socket()
print(socket.socket)

#--
import select
print(select.select)
monkey.patch_select()
print("After monkey patch")
print(select.select)
