import Tkinter as Tk
import pickle
import sys
from ctypes import *
from multiprocessing import Process

import Waiter
from settings import *


class TransparentWin (Tk.Tk) :
    ''' Transparent Tk Window Class '''

    def __init__ (self, mouse_width_starting_position, mouse_height_starting_position) :

        Tk.Tk.__init__(self)
        global globalna
        # globalna.put("Transmission STARTED!")
        self.mouse_height_starting_position = mouse_height_starting_position
        self.mouse_width_starting_position = mouse_width_starting_position
        self.screen_width = self.winfo_vrootwidth()
        self.screen_height = self.winfo_vrootheight()
        self.width_to_destroy_transparantwin = self.screen_width - 2
        print self.screen_width
        print self.screen_height
        print 'height ' + str(mouse_height_starting_position)
        print 'width '  + str(mouse_width_starting_position)


        # self.focus_force()
        self.overrideredirect(True)
        self.resizable(False, False)
        self.wm_attributes("-topmost", True)
        self.attributes("-alpha", 0.2)
        #Reset mouse position
        windll.user32.SetCursorPos(self.screen_width -2, mouse_height_starting_position)
        sys.setrecursionlimit(10000)

        self.create_transparent_widget()
        # self.config(cursor="none")
        self.q = Queue.Queue()

    def get_mouse_position(self, event):
        pozycjax = self.winfo_pointerx()
        pozycjay = self.winfo_pointery()
        print('{},{}'.format(pozycjax, pozycjay))

    def create_transparent_widget(self):
        bg = '#3e4134'
        self.Frame = Tk.Frame(self, bg=bg)
        self.Frame.pack()

        ''' Exits the application when the window is right clicked. '''

        self.x_previous = self.screen_width -2
        self.y_previous = self.mouse_height_starting_position
        self.Frame.bind('<Motion>', lambda event: self.get_mouse_position_delta(event, self.x_previous, self.y_previous))
        self.bind('<MouseWheel>', self.get_mouse_wheel_down)
        self.Frame.bind('<Button-1>', self.get_mouse_left_click)
        self.Frame.bind('<ButtonRelease-1>', self.get_mouse_left_released)
        self.Frame.bind('<B1-Motion>', self.get_mouse_left_hold)
        self.Frame.bind('<Button-3>', self.exit)


        ''' Changes the window's size indirectly. '''
        self.Frame.configure(width=self.screen_width, height=self.screen_height)

    def get_mouse_wheel_down(self, event):
        # print event
        if event.num == 5 or event.delta == -120:
            print("Scroll down")
            globalna.put("Scroll down")
        if event.num == 4 or event.delta == 120:
            print("Scroll up")
            globalna.put("Scroll up")

    def get_mouse_left_released(self, event):
        global globalna
        globalna.put("Left mouse button was released")
        print("Left mouse button was released")

    def get_mouse_left_hold(self, event):
        global globalna
        globalna.put("Left button is holded")
        print("Left button is holded")

    def get_mouse_left_click(self, event):
        global globalna
        globalna.put("Left click")
        print("Left click")

    def get_mouse_position_delta(self, event, x_previous_width, y_previous_height):
        width, height = event.x, event.y

        self.xdelta = width - x_previous_width
        self.ydelta = height - y_previous_height
        self.x_previous = width
        self.y_previous = height
        tup = (self.xdelta, self.ydelta,)
        if width > self.width_to_destroy_transparantwin:
            p1 = Process(target=self.destroy())
            p2 = Process(target=Waiter.Waiter(height).mainloop())
            p1.start()
            p2.start()

        to_send = pickle.dumps(tup)
        global globalna
        globalna.put(to_send)
        # print tup
        # a, b = tup
        # print a
        # print b
        # globalna.put(str(self.xdelta) + ',' + str(self.ydelta))
        # print str(self.xdelta) + ',' + str(self.ydelta)
        # globalna.put('{},{}'.format(self.xdelta, self.ydelta))
        print('Parametr x: {}, Parameter y: {}'.format(self.xdelta, self.ydelta))

    def exit (self, event) :
        self.destroy()

def __run__ () :

    TransparentWin().mainloop()


if __name__ == '__main__' :

    __run__()