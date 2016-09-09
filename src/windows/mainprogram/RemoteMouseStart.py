import Tkinter as Tk, re
from MouseCoordinates import MouseCoordinates


class TransparentWin (Tk.Tk) :
    ''' Transparent Tk Window Class '''

    def __init__ (self) :

        Tk.Tk.__init__(self)

        screen_width = self.winfo_vrootwidth()
        screen_height = self.winfo_vrootheight()
        print screen_width
        print screen_height

        ''' Sets focus to the window. '''
        self.focus_force()

        ''' Removes the native window boarder. '''
        self.overrideredirect(True)

        ''' Disables resizing of the widget.  '''
        self.resizable(False, False)

        ''' Places window above all other windows in the window stack. '''
        self.wm_attributes("-topmost", True)

        ''' This changes the alpha value (How transparent the window should
            be). It ranges from 0.0 (completely transparent) to 1.0
            (completely opaque).  '''

        self.attributes("-alpha", 0.2)

        ''' The windows overall position on the screen  '''
        self.wm_geometry('+' + str(0) + '+' + str(0))

        ''' Changes the window's color. '''
        bg = '#3e4134'

        self.config(bg=bg)
        self.config(cursor="none")

        self.Frame = Tk.Frame(self, bg=bg)
        self.Frame.pack()

        ''' Exits the application when the window is right clicked. '''
        # self.Frame.bind('<Motion>', self.get_mouse_position)
        self.Frame.bind('<Motion>', MouseCoordinates.get_mouse_position())
        self.Frame.bind('<Button-3>', self.exit)

        ''' Changes the window's size indirectly. '''
        self.Frame.configure(width=screen_width, height=screen_height)

    # def get_mouse_position(self, event):
    #     x, y = event.x, event.y
    #     print('{}, {}'.format(x, y))

    def exit (self, event) :
        self.destroy()

def __run__ () :

    TransparentWin().mainloop()


if __name__ == '__main__' :

    __run__()