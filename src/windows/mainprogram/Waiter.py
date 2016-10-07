import Tkinter as Tk
from ctypes import *
from multiprocessing import Process

import RemoteMouseStart


class Waiter(Tk.Tk):

    def __init__(self, mouse_height_starting_position):

        # self.q = Queue.Queue()
        Tk.Tk.__init__(self)

        self.screen_width = self.winfo_vrootwidth()
        self.screen_height = self.winfo_vrootheight()
        print self.screen_width
        print self.screen_height

        # thread_with_server = threading.Thread(target=self.create_server)
        # thread_with_server.start()
        windll.user32.SetCursorPos(3, mouse_height_starting_position)
        self.overrideredirect(True)
        self.resizable(False, False)
        self.wm_attributes("-topmost", True)
        self.attributes("-alpha", 0.2)

        self.create_transparent_widget()

    def create_transparent_widget(self):
        bg = '#3e4134'
        self.Frame = Tk.Frame(self, bg=bg)
        self.Frame.pack()

        ''' Exits the application when the window is right clicked. '''

        self.x_previous = 0
        self.y_previous = 0
        self.Frame.bind('<Motion>', lambda event: self.turn_on_transparentwin(event))

        ''' Changes the window's size indirectly. '''
        self.Frame.configure(width=2, height=self.screen_height)


    def turn_on_transparentwin(self, event):
        width, height = event.x, event.y
        print('{}, {}'.format(width, height))
        p1 = Process(target=self.destroy())
        p2 = Process(target=RemoteMouseStart.TransparentWin(width, height).mainloop())
        p1.start()
        p2.start()


    def get_mouse_position_delta(self, event, x_previous, y_previous):
        x, y = event.x, event.y

        self.xdelta = x - x_previous
        self.ydelta = y - y_previous
        self.x_previous = x
        self.y_previous = y
        print('Parametr x: {}, Parameter y: {}'.format(self.xdelta, self.ydelta))

    # def create_server(self):
    #     HOST = ''
    #     PORT = 8888
    #
    #     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     print "Socket has been created"
    #
    #     try:
    #         s.bind((HOST, PORT))
    #     except socket.error, msg:
    #         print "Bind has failed. Error code: " + str(msg[0]) + " Message brzmi: " + msg[1]
    #         sys.exit()
    #
    #     print "Bind has succeeded"
    #
    #     s.listen(10)
    #     print "Socket waits for connections"
    #
    #     while 1:
    #         conn, addr = s.accept()
    #         print "Connected with: " + addr[0] + " : " + str(addr[1])
    #         start_new_thread(self.client_thread,(conn, ))
    #
    #     s.close()

    # def client_thread(self, conn):
    #
    #     conn.send("Welcome. You are connected")
    #
    #     # message = raw_input("Wyslij komende")
    #     # global globalna
    #     # globalna.put(message)
    #
    #     # self.q.put(message)
    #
    #     while globalna:
    #         conn.send(globalna.get())
    #         if not globalna:
    #             break
    #         # message = raw_input("Wyslij komende")
    #         # globalna.put(message)
    #     conn.close()

def __run__ () :

    Waiter().mainloop()

if __name__ == '__main__' :
    __run__()