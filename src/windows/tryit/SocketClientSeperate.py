import socket
import sys


host = '127.0.0.1'
port = 8888
try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print "Failed bo. Errorkod:" + str(msg[0]), "Error message : " + msg[1]
    sys.exit()

mySocket = socket.socket()
mySocket.connect((host,port))

# message = raw_input(" napisz cpos ")

while True:
    # mySocket.send(message)
    # mySocket.send(message.encode())
    # data = mySocket.recv(1024).decode()
    data = mySocket.recv(1024)
    if not data: break
    print ('Received from server: ' + data)


    # message = raw_input(" ? ")

mySocket.close()