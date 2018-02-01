#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
fileimage = "testimage.jpg"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
print "send data:", fileimage
fileOpen = open(fileimage,'rb')
data = fileOpen.read(BUFFER_SIZE)
while (data):
    s.send(data)
    data = fileOpen.read(BUFFER_SIZE)
fileOpen.close()
print "done send"
s.close()

    

