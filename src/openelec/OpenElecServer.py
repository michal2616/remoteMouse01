import socket
import sys
from thread import *

class OpenElecServer:

    def __init__(self):
        self.create_server()


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

        while 1:
            data = conn.recv(1024)
            if not data: break
            # pyautogui.press("k")
            print data
        conn.close()

def __run__ () :

    OpenElecServer()

if __name__ == '__main__' :
    __run__()