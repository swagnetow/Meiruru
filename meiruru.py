#!/usr/bin/python2.7

# Verified using FakeSMTP (http://nilhcem.github.com/FakeSMTP/)

import socket

s = socket.socket()
host = "127.0.0.1"
port = 2525

s.connect((host, port))
print s.recv(512)

s.send("HELO localhost\r\n")
print s.recv(512)

s.send("MAIL FROM: <example@example.com>\r\n")
print s.recv(512)

s.send("RCPT TO: <example@example.com>\r\n")
print s.recv(512)

s.send("DATA\r\n")
s.send("Subject: Hi!\r\n")
s.send("\r\n")
s.send("Bye!\r\n")
print s.recv(512)

s.send(".\r\n")
print s.recv(512)

s.send("QUIT\r\n")
print s.recv(512)

s.close
