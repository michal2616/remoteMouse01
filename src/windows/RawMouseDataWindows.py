from ctypes import windll, Structure, c_ulong, byref
# import ctypes
# import Wx


class POINT(Structure):


    # _fields_ = [("x", c_ulong), ("y", c_ulong)]
    #
    # # user32 = windll.user32
# # user32.SetProcessDPIAware()
# #
# # screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
# #
# print screensize
#
    def queryMousePosition():
        pt = POINT()
        windll.user32.GetCursorPos(byref(pt))
        return {"x": pt.x, "y": pt.y}


# print screensize
    pos = queryMousePosition()
    while 1:
        print(pos)