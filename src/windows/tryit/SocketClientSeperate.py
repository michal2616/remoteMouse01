import socket
import sys

import pyautogui

host = '192.168.1.222'
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

while 1:
    # mySocket.send(message)
    # mySocket.send(message.encode())
    # data = mySocket.recv(1024).decode()
    data = mySocket.recv(1024)
    if not data: break
    pyautogui.press(datakkkkk)

    # list_with_width_coordinates = data.split(";")
    # print list_with_width_coordinates
    #
    # for member in list_with_width_coordinates:
    #     seperate_coordinates_list = member.split(",")
    #     print member
    #     if seperate_coordinates_list[0]:
    #         memberX_to_int = float(seperate_coordinates_list[0]) * float(1.8)
    #         memberY_to_int = float(seperate_coordinates_list[1]) * float(1.5)
    #         pyautogui.moveRel(memberX_to_int, memberY_to_int)



        # print member_to_int
        # print type(member_to_int)

    # print 'parametr x: ' + str(load_data[0])
    # szerokosc = int(load_data[0]) * float(1.8)
    # print szerokosc
    # print 'parametr y : ' + str(load_data[1])
    # wysokosc = int(load_data[1]) * float(1.35)
    # print wysokosc

    # print 'wysokosc ' + move_order[1]
    # print ('Received from server: Width' + move_order[jakas -2] + ' Height: ' + move_order[jakas -1])
    # pyautogui.moveRel(load_data[0], load_data[1])
    # pyautogui.moveRel(szerokosc, wysokosc, duration=0.1)
    # pyautogui.dragRel(szerokosc, wysokosc, duration=num_seconds)
    # print ('Received from server: Width' + data +' Height: ')

    # message = raw_input(" ? ")

mySocket.close()