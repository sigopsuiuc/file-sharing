from watchdog.events import LoggingEventHandler, RegexMatchingEventHandler
import logging
from multiprocessing import Queue
import socket
import json
import sqlite3
import os
import hashlib
import datetime
import time

class P2PFSEventHandler(RegexMatchingEventHandler):

    # ignore_regexes=['^.+?\.sw.?$']
    deleted = "deleted"
    modified = "modified"
    moved = "moved"
    created = "created"

    def __init__(self, metadata_dir, sharing_dir, user):
        super(P2PFSEventHandler, self).__init__(ignore_regexes=['^.+?\.sw.?$'])  #ignore temporary files
        self._eventqueue = Queue()
        self.sharing_dir = sharing_dir
        dir_db = metadata_dir + '/peers.db'
        if os.path.exists(dir_db):
            self._conn_db = sqlite3.connect(dir_db)
            self._c_db    = self._conn_db.cursor()
        else:
            self._conn_db = sqlite3.connect(dir_db)
            self._c_db    = self._conn_db.cursor()
            self._c_db.execute('''CREATE TABLE peers
                (name text, ip text, port int, PRIMARY KEY(name DESC))''')

        self.user = user
        self.metadata_dir = metadata_dir








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

    def process_event(self, local_port):
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
            #TODO: get time, and number
            today = str(datetime.date.today())
            # check_sum = self.md5(event.src_path)
            timestamp = time.time()
            path = event.src_path.replace(self.sharing_dir, "")
            event_l = [event.event_type, event.is_directory, path, '127.0.0.1',
                       local_port, today, timestamp]
            print event_l
            conn = sqlite3.connect(self.metadata_dir + '/files.db')
            cursor = conn.cursor()
            # TODO: We need to change here
            cursor.execute("INSERT OR REPLACE INTO files (dir, time) VALUES (?,?)", (path, timestamp))
            conn.commit()
            conn.close()

            for row in self._c_db.execute('SELECT * FROM peers'):
                if row[0] != self.user:
                    try:
                        event_sent = json.dumps(event_l)
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((row[1], row[2]))
                        s.send("event: " + event_sent)
                        s.close()
                    except socket.error as msg:
                        print "socket error in eventhandler " + str(msg)
                        continue


            #indicator_queue.put(event)

    def md5(self, fname):
        if os.path.isdir(fname):
            return ""
        hash = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash.update(chunk)
        return hash.hexdigest()
