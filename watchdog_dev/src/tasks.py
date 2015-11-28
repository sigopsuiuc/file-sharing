from multiprocessing import Process, Queue
from eventhandler import P2PFSEventHandler



class Coordinator:

    def __init__(self, event_handler, connector):
        self.tcp_busy = False
        self._event_handler = event_handler
        self.indicator = connector.indicator
        self.connector = connector
        #self._tcp_lock = Lock()



    def tasklet(self):
        #TODO
        #check for incoming traffic
        if self.tcp_busy:
            raise CoordinationException("tcp is busy now!")
            return

        #check the event queue
        self._event_handler.process_event(self.indicator.debug_eventqueue)
        #update the files(send out files)


    def start(self):
        self.connector.start()

    def terminate(self):
        self.connector.terminate()

    def join(self):
        self.connector.join()

    class CoordinationException(Exception):

        def __init__(self, value):
            self.value = value

        def __str__(self):
            repr(self.value)

class Connector:

    def __init__(self, client, server, senderport, receiverport, indicator):
        self.clientProcess = Process(target = client, args=(senderport, indicator.debug_eventqueue,))
        self.clientProcess.daemon = True
        self.serverProcess = Process(target = server, args=(receiverport,))
        self.serverProcess.daemon = True
        self.indicator = indicator

    def start(self):
        self.clientProcess.start()
        self.serverProcess.start()

    def terminate(self):
        self.clientProcess.terminate()
        self.serverProcess.terminate()

    def join(self):
        self.clientProcess.join()
        self.serverProcess.join()

class Indicator:

    def __init__(self):
        self.debug_eventqueue = Queue()
