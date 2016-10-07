import pickle
import socket
import sys

import pyautogui

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
    # move_order = data.split(",")
    # jakas = len(move_order)
    if not data: break

    # parse_width = int(float((move_order[0])))
    # parse_height = int(float((move_order[1])))
    # parse_width2 = parse_width * (-1)
    # parse_height2 = parse_height * (-1)
    load_data = pickle.loads(data)
    print load_data[0]
    print load_data[1]
    # print 'wysokosc ' + move_order[1]
    # print ('Received from server: Width' + move_order[jakas -2] + ' Height: ' + move_order[jakas -1])
    pyautogui.moveRel(load_data[0], load_data[1])
    # print ('Received from server: Width' + data +' Height: ')

    # message = raw_input(" ? ")

mySocket.close()