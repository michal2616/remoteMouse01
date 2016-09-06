import Tkinter as Tk, re




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
        self.Frame.bind('<Button-3>', self.exit)

        ''' Changes the window's size indirectly. '''
        self.Frame.configure(width=screen_width, height=screen_height)

    def exit (self, event) :
        self.destroy()

    def drag_wid (self, event) :

        cx, cy = self.Par.winfo_pointerxy()

        d = self.Dissable

        if d == 'x' :
            x = self.OriX
            y = cy - self.RelY
        elif d == 'y' :
            x = cx - self.RelX
            y = self.OriY
        else:
            x = cx - self.RelX
            y = cy - self.RelY

        if x < 0 :
            x = 0

        if y < 0 :
            y = 0

        self.Par.wm_geometry('+' + str(x) + '+' + str(y))

    def drag_unbind (self, event) :

        self.Par.unbind('<Motion>')

        if self.ReleaseCMD != None :
            self.ReleaseCMD()


    # def dissable (self) :
    #
    #     self.Par.unbind('<Button-1>')
    #     self.Par.unbind('<ButtonRelease-1>')
    #     self.Par.unbind('<Motion>')


def __run__ () :

    TransparentWin().mainloop()


if __name__ == '__main__' :

    __run__()