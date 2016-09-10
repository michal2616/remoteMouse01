import Tkinter as Tk, re

class MouseCoordinates():

    def get_mouse_position(self, event):
        x, y = event.x, event.y
        print('{}, {}'.format(x, y))


# this has to be added in main loop program to use get_mouse_position function:
# self.Frame.bind('<Motion>', lambda event: MouseCoordinates.get_mouse_position(MouseCoordinates(), event))

# and import there:
# from MouseCoordinates import MouseCoordinates