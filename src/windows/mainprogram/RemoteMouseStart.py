import Tkinter as Tk


class TransparentWin (Tk.Tk) :
    ''' Transparent Tk Window Class '''

    def __init__ (self) :

        Tk.Tk.__init__(self)

        self.screen_width = self.winfo_vrootwidth()
        self.screen_height = self.winfo_vrootheight()
        print self.screen_width
        print self.screen_height



        # self.focus_force()
        self.overrideredirect(True)
        self.resizable(False, False)
        self.wm_attributes("-topmost", True)
        self.attributes("-alpha", 0.2)

        self.create_transparent_widget()

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
        self.Frame.bind('<Button-3>', self.exit)

        ''' Changes the window's size indirectly. '''
        self.Frame.configure(width=self.screen_width, height=self.screen_height)

    def get_mouse_position_delta(self, event, x_previous, y_previous):
        x, y = event.x, event.y

        self.xdelta = x - x_previous
        self.ydelta = y - y_previous
        self.x_previous = x
        self.y_previous = y
        print('Parametr x: {}, Parameter y: {}'.format(self.xdelta, self.ydelta))

    def exit (self, event) :
        self.destroy()

def __run__ () :

    TransparentWin().mainloop()


if __name__ == '__main__' :

    __run__()