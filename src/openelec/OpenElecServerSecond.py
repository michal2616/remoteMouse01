import socket
import sys
from thread import *

import pyautogui


class OpenElecServerSecond:

    def __init__(self):
        pyautogui.FAILSAFE = False
        self.create_server()


    def create_server(self):
        HOST = '192.168.1.222'
        PORT = 8889

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
            data = conn.recv(8)
            if not data: break
            print data
            splited_data = data.split(',')
            print splited_data

            for member in splited_data:
                if member == "u":
                    pyautogui.scroll(200)
                if member == "l":
                    pyautogui.click()
                if member == "d":
                    pyautogui.scroll(-200)

            # pyautogui.press("k")


            # pyautogui.moveRel(memberX_to_int, memberY_to_int)


def __run__ () :

    OpenElecServerSecond()

if __name__ == '__main__' :
    __run__()