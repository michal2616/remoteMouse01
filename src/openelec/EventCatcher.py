import Tkinter as Tk

from StaticData import *


class EventCatcher (Tk.Tk) :
    ''' Transparent Tk Window Class '''

    def __init__ (self) :

        Tk.Tk.__init__(self)
        global globalQueue
        globalQueue.put("Transmission STARTED!")
        self.screen_width = self.winfo_vrootwidth()
        self.screen_height = self.winfo_vrootheight()
        self.width_to_destroy_event_catcher = self.screen_width - 2
        print self.screen_width
        print self.screen_height

        # self.focus_force()
        self.overrideredirect(True)
        self.resizable(False, False)
        self.wm_attributes("-topmost", True)
        self.attributes("-alpha", 0.2)

        self.create_transparent_widget()
        # self.config(cursor="none")
        self.q = Queue.Queue()

    def get_mouse_position(self, event):
        width, height = event.x, event.y
        print('Width: {},Height: {}'.format(width, height))

    def create_transparent_widget(self):
        bg = '#3e4134'
        self.Frame = Tk.Frame(self, bg=bg)
        self.Frame.pack()

        ''' Exits the application when the window is right clicked. '''

        self.Frame.bind('<Motion>', lambda event: self.get_mouse_position(event))
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
            globalQueue.put("Scroll down")
        if event.num == 4 or event.delta == 120:
            print("Scroll up")
            globalQueue.put("Scroll up")

    def get_mouse_left_released(self, event):
        global globalQueue
        globalQueue.put("Left mouse button was released")
        print("Left mouse button was released")

    def get_mouse_left_hold(self, event):
        global globalQueue
        globalQueue.put("Left button is holded")
        print("Left button is holded")

    def get_mouse_left_click(self, event):
        global globalQueue
        globalQueue.put("Left click")
        print("Left click")

    def exit (self, event) :
        self.destroy()

def __run__ () :

    EventCatcher().mainloop()


if __name__ == '__main__' :

    __run__()