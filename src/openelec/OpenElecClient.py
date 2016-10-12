import socket
import sys

from StaticData import *


class OpenElecClient:

    def __init__(self):
        self.create_client()

    def create_client(self):
        host = '127.0.0.1'
        port = 8888
        try:
            #create an AF_INET, STREAM socket (TCP)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error, msg:
            print "Failed bo. Errorkod:" + str(msg[0]), "Error message : " + msg[1]
            sys.exit()

        s.connect((host,port))

        while globalQueue.get():
            s.send(globalQueue.get())
            if not globalQueue.get(): break

        s.close()

def __run__ () :

    OpenElecClient()

if __name__ == '__main__' :
    __run__()