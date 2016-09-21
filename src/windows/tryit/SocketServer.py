import socket
import sys
from thread import *

HOST = ''
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Socket stworzone"

try:
    s.bind((HOST, PORT))
except socket.error, msg:
    print "Bind sie nie udalo. Eror code: " + str(msg[0]) + " Messsag brzmi: " + msg[1]
    sys.exit()

print "Socket bind jest gotowe, ale musi jeszcze zaczac nasluchiwac"

s.listen(10)
print "Teraz socket zaczal nasluchiwac"

# while 1:
#     conn, addr = s.accept()
#     data = conn.recv(1024)
#     print "POlaczony z " + addr[0] + " : " + str(addr[1])
#     reply = "OK ... " + data
#     print data
#     if not data:
#         break
#     conn.sendall(reply)
#
# conn.close()
# s.close()

def clientthread(conn):
    conn.send("welcome. zostales polaczony")

    while True:
        data = conn.recv(1024)
        reply = "OK ... " + data
        print data
        # if not data:
        # break
        conn.sendall(reply)
    conn.close()

while 1:
    conn, addr = s.accept()
    print "POlaczony z " + addr[0] + " : " + str(addr[1])
    start_new_thread(clientthread,(conn, ))

s.close()

# http://www.binarytides.com/python-socket-programming-tutorial/
# https://www.tutorialspoint.com/python/python_networking.htm