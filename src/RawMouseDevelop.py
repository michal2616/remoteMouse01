import struct

file = open( "/dev/input/mice", "rb" );

def getMouseEvent():
    buf = file.read(3);
    # button = ord( buf[0] );
    # print button
    # bLeft = button & 0x1;
    # bMiddle = ( button & 0x4 ) > 0;
    # bRight = ( button & 0x2 ) > 0;
    x,y = struct.unpack( "bb", buf[1:] );
    print ("x: %d, y: %d\n" % (x, y) );
    return x, y;


a = 0
b = 0
while 1:
    q, w =getMouseEvent();
    a = a + q
    b = b + w
    print "Wyswietla zmienne %d, %d" % (a,b)
file.close();