import Tkinter as Tk, re

class MouseCoordinates():

    def get_mouse_position(self, event):
        x, y = event.x, event.y
        print('{}, {}'.format(x, y))


# this has to be added in main loop program to use turn_on_transparentwin function:
# self.Frame.bind('<Motion>', lambda event: MouseCoordinates.turn_on_transparentwin(MouseCoordinates(), event))

# and import there:
# from MouseCoordinates import MouseCoordinates