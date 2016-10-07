import socket
import sys
import threading
from multiprocessing import Process
from thread import *

import Waiter
from settings import *


class ServerInvoker:

    def __init__(self):
        thread_with_server = threading.Thread(target=self.create_server)

        # p1 run server that listen on port 8888
        # p2 run Waiter class that waits to start data transmission when mouse is on the left edge of the screen
        p1 = Process(target=thread_with_server.start())
        p2 = Process(target=Waiter.Waiter(500).mainloop())

    def create_server(self):
        HOST = ''
        PORT = 8888

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print "Socket has been created"

        try:
            s.bind((HOST, PORT))
        except socket.error, msg:
            print "Bind has failed. Error code: " + str(msg[0]) + " Message brzmi: " + msg[1]
            sys.exit()

        print "Bind has succeeded"

        s.listen(10)
        print "Socket waits for connections"

        while 1:
            conn, addr = s.accept()
            print "Connected with: " + addr[0] + " : " + str(addr[1])
            start_new_thread(self.client_thread,(conn, ))

        s.close()

    def client_thread(self, conn):

        # conn.send("Welcome. You are connected")

        while globalna:
            conn.send(globalna.get())
            if not globalna:
                break

        conn.close()

def __run__ () :

    ServerInvoker()

if __name__ == '__main__' :
    __run__()