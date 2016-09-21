import socket
import sys

try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print "Failed bo. Errorkod:" + str(msg[0]), "Error message : " + msg[1]
    sys.exit()

print "Socket stworzony"

host = '127.0.0.1'
port = 8888
# try:
#     remote_ip = socket.gethostbyname( host )
# except socket.gaierror:
#     print "Can't resolv host"
#     sys.exit()

# print "Ip address of " + host + " is " + remote_ip

s.connect((host, port))

# print "Soccket connected to " + host + " on ip " + remote_ip

#Send some data to remote server
message = "GET down"

try :
    #Set the whole string
    s.sendall(message)
except socket.error:
    #Send failed
    print 'Send failed'
    sys.exit()

print 'Message zostala wyslana successfully'

#Now receive data
reply = s.recv(4096)

print reply

s.close()