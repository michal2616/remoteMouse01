import threading

import EventCatcher
import OpenElecClient


class ClientInvoker:

    def __init__(self):
        client_thread = threading.Thread(OpenElecClient.OpenElecClient())
        event_catcher_thread = threading.Thread(target= EventCatcher.EventCatcher.mainloop())

        event_catcher_thread.start()
        client_thread.start()
        # EventCatcher.EventCatcher.mainloop()

def __run__ () :

    ClientInvoker()


if __name__ == '__main__' :

    __run__()
