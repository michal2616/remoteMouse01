import socket
import sys
from thread import *

import pyautogui


class OpenElecServer:

    def __init__(self):
        pyautogui.FAILSAFE = False
        self.create_server()


    def create_server(self):
        HOST = '192.168.1.222'
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
            width_ratio = 1
            height_ratio = 1
            if not data: break
            # pyautogui.press("k")
            # print data
            list_with_width_coordinates = data.split(";")
            # print list_with_width_coordinates

            seperate_coordinates = list_with_width_coordinates[-2].split(",")
            width = int(seperate_coordinates[0]) * width_ratio
            height = int(seperate_coordinates[1]) * height_ratio
            # print width
            # print height
            # print ""
            pyautogui.moveTo(width, height,0.1 ,pyautogui.linear(1))
                    # pyautogui.moveRel(memberX_to_int, memberY_to_int)


def __run__ () :

    OpenElecServer()

if __name__ == '__main__' :
    __run__()