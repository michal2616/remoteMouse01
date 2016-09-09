import Tkinter as Tk, re

class MouseCoordinates():

    def get_mouse_position(self, event):
        x, y = event.x, event.y
        print('{}, {}'.format(x, y))