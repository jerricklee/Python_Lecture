__author__ = 'jerrick'

from socket import *
svrSock = socket(AF_INET, SOCK_STREAM)
svrSock.connect(('127.0.0.1', 2000))
svrSock.send(b"Hell")