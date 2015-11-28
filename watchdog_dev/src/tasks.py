from multiprocessing import Process
from eventhandler import P2PFSEventHandler

class Coordinator:

    def __init__(self, event_handler):
        self.tcp_busy = False
        self._event_handler = event_handler
        #self._tcp_lock = Lock()



    def tasklet(self):
        #TODO
        #check for incoming traffic
        if self.tcp_busy:
            raise CoordinationException("tcp is busy now!")
            return


        #check the event queue
        self._event_handler.process_event()
        #update the files(send out files)

    class CoordinationException(Exception):

        def __init__(self, value):
            self.value = value

        def __str__(self):
            repr(self.value)

class Connector:

    def __init__(self, client, server, senderport, receiverport):
        self.clientProcess = Process(target = client, args=(senderport,))
        self.clientProcess.daemon = True
        self.serverProcess = Process(target = server, args=(receiverport,))
        self.serverProcess.daemon = True

    def start(self):
        self.clientProcess.start()
        self.serverProcess.start()

    def terminate(self):
        self.clientProcess.terminate()
        self.serverProcess.terminate()

    def join(self):
        self.clientProcess.join()
        self.serverProcess.join()
