from pymouse import PyMouse
from pykeyboard import PyKeyboard
import threading

print "jakis napis"

m = PyMouse()

# while(True):
#     print m.position()


def printit():
    threading.Timer(0.5, printit).start()
    print m.position()

printit()

print "inny napis"