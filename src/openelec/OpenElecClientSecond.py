import socket
import sys
import thread

import StaticData


class OpenElecClientSecond:
    def __init__(self):

        self.create_client()

    def create_client(self):
        # host = '127.0.0.1'
        host = '192.168.1.222'
        port = 8889
        try:
            #create an AF_INET, STREAM socket (TCP)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error, msg:
            print "Failed bo. Errorkod:" + str(msg[0]), "Error message : " + msg[1]
            sys.exit()

        try:
            s.connect((host,port))
        except socket.error, msg:
            print "ege szege dre. Serwer wlaczony? " + str(msg)
            thread.exit_thread()

        # global globalQueue

        sending_queue_second = StaticData.globalQueueSecond
        while sending_queue_second:
            s.send(sending_queue_second.get())
            if not sending_queue_second: break

        s.close()

def __run__ () :

    OpenElecClientSecond()

if __name__ == '__main__' :
    __run__()