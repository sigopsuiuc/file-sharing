from watchdog.events import LoggingEventHandler, RegexMatchingEventHandler
import logging
from multiprocessing import Queue
import socket
import json

class P2PFSEventHandler(RegexMatchingEventHandler):

#ignore_regexes=['^.+?\.sw.?$']
    deleted = "deleted"
    modified = "modified"
    moved = "moved"
    created = "created"

    def __init__(self):
        super(P2PFSEventHandler, self).__init__(ignore_regexes=['^.+?\.sw.?$']) #ignore temporary files
        self._eventqueue = Queue()


    def on_deleted(self, event):
        super(P2PFSEventHandler, self).on_deleted(event)
        print("ahha we are deleting something")
        self._eventqueue.put(event)
        what = 'directory' if event.is_directory else 'file'
        logging.info("Deleted %s: %s", what, event.src_path)

    def on_moved(self, event):
        super(P2PFSEventHandler, self).on_moved(event)
        print("aha we are moving something")
        self._eventqueue.put(event)
        what = 'directory' if event.is_directory else 'file'
        logging.info("Moved %s: from %s to %s", what, event.src_path,
                     event.dest_path)

    def on_modified(self, event):
        super(P2PFSEventHandler, self).on_modified(event)
        print("aha we are modifying something")
        self._eventqueue.put(event)
        what = 'directory' if event.is_directory else 'file'
        logging.info("Modified %s: %s", what, event.src_path)

    def on_created(self, event):
        super(P2PFSEventHandler, self).on_created(event)
        print("ahhh we are creating something")
        self._eventqueue.put(event)
        what = 'directory' if event.is_directory else 'file'
        logging.info("Created %s: %s", what, event.src_path)


    def process_event(self, remote_socket_dict, local_port):
        if self._eventqueue.empty():
            return
        event = self._eventqueue.get()

        event_t = event.event_type
        if event_t is self.deleted:
            #print("1111111")
            pass
        elif event_t is self.modified:
            if not event.is_directory:
                #print("2222222")
                pass
        elif event_t is self.moved:
            #print("3333333")
            pass
        elif event_t is self.created:
            print("4444444")
            #TODO: What we really want to do here is to send a TCP notification
            #      to All the peers
            for (key, value) in remote_socket_dict.items():
                try:
                    event_l = [event.event_type, event.is_directory, event.src_path, '127.0.0.1', local_port]
                    event_sent = json.dumps(event_l)
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((value[0], value[1]))
                    s.send("event: " + event_sent)
                    s.close()
                except socket.error as msg:
                    print "socket error in eventhandler " + msg
                    continue


            #indicator_queue.put(event)