import Tkinter as Tk
import Waiter
from multiprocessing import Process

class TransparentWin (Tk.Tk) :
    ''' Transparent Tk Window Class '''

    def __init__ (self) :

        Tk.Tk.__init__(self)

        self.screen_width = self.winfo_vrootwidth()
        self.screen_height = self.winfo_vrootheight()
        self.width_to_destroy_transparantwin = self.screen_width - 2
        print self.screen_width
        print self.screen_height

        # self.focus_force()
        self.overrideredirect(True)
        self.resizable(False, False)
        self.wm_attributes("-topmost", True)
        self.attributes("-alpha", 0.2)

        self.create_transparent_widget()
        # self.config(cursor="none")

    def get_mouse_position(self, event):
        pozycjax = self.winfo_pointerx()
        pozycjay = self.winfo_pointery()
        print('{},{}'.format(pozycjax, pozycjay))

    def create_transparent_widget(self):
        bg = '#3e4134'
        self.Frame = Tk.Frame(self, bg=bg)
        self.Frame.pack()

        ''' Exits the application when the window is right clicked. '''

        self.x_previous = 0
        self.y_previous = 0
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
        if event.num == 4 or event.delta == 120:
            print("Scroll up")

    def get_mouse_left_released(self, event):
        print("Left mouse button was released")

    def get_mouse_left_hold(self, event):
        print("Left button is holded")

    def get_mouse_left_click(self, event):
        print("Left click")

    def get_mouse_position_delta(self, event, x_previous, y_previous):
        x, y = event.x, event.y

        self.xdelta = x - x_previous
        self.ydelta = y - y_previous
        self.x_previous = x
        self.y_previous = y
        if x > self.width_to_destroy_transparantwin:
            p1 = Process(target=self.destroy())
            p2 = Process(target=Waiter.Waiter().mainloop())
            p1.start()
            p2.start()
            self.destroy()
        print('Parametr x: {}, Parameter y: {}'.format(self.xdelta, self.ydelta))

    def exit (self, event) :
        self.destroy()

def __run__ () :

    TransparentWin().mainloop()


if __name__ == '__main__' :

    __run__()