from ctypes import windll, Structure, c_ulong, byref
import time
# import win32api


class POINT(Structure):

    _fields_ = [("x", c_ulong), ("y", c_ulong)]



def queryMousePosition(event):
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    print { "x": pt.x, "y": pt.y}



while 1:
    pos = queryMousePosition()
    print(pos)
    time.sleep(.01)