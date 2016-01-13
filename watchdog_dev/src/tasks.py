from multiprocessing import Process, Queue, Manager
from eventhandler import P2PFSEventHandler
from messenger import Messenger


class Coordinator:

    def __init__(self, event_handler, connector, receiverport):
        self.tcp_busy = False
        self._event_handler = event_handler
        self.indicator = connector.indicator
        self.connector = connector
        
        self.receiverport = receiverport

        #self._tcp_lock = Lock()



    def tasklet(self):
        #TODO
        #check for incoming traffic
        if self.tcp_busy:
            raise CoordinationException("tcp is busy now!")
            return

        #check the event queue
        #if self.peer_group_dict:
        #    print self.peer_group_dict
        self._event_handler.process_event(self.receiverport)
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

    def __init__(self, client, server, receiverport, messenger_port, indicator, sharing_directory,
                metadata_dir):
        self.clientProcess = Process(target = client, args=(indicator.debug_eventqueue,
                                                            sharing_directory, metadata_dir, ))
        self.clientProcess.daemon = True
        self.serverProcess = Process(target = server, args=(receiverport, sharing_directory, indicator.debug_eventqueue, ))
        self.serverProcess.daemon = True
        self.indicator = indicator
        self.my_messenger = Messenger(messenger_port, metadata_dir)
        self.messengerProcess = Process(target = self.my_messenger.process, args=(indicator.debug_eventqueue, ))
        self.messengerProcess.daemon = True


    def start(self):
        self.clientProcess.start()
        self.serverProcess.start()
        self.messengerProcess.start()

    def terminate(self):
        self.clientProcess.terminate()
        self.serverProcess.terminate()
        self.messengerProcess.terminate()


    def join(self):
        self.clientProcess.join()
        self.serverProcess.join()
        self.messengerProcess.join()

class Indicator:

    def __init__(self):
        self.debug_eventqueue = Queue()
