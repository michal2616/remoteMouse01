from ctypes import *
from random import randint
user = windll.user32

while 1:
    x = randint(0, 3840)
    y= randint(0, 1080)
    user.SetCursorPos(x,y)