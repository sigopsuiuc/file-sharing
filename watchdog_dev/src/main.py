import sys
import os
import time
import logging
#import multiprocessing
from watchdog.observers import Observer
#from watchdog.events import LoggingEventHandler
from eventhandler import P2PFSEventHandler
from tasks import Coordinator, Connector, Indicator
from multiprocessing import Manager
import client
import server
import sqlite3


def check_directories(user):
    dir = os.path.dirname(__file__)
    metadata = os.path.join(dir, '../metadata', user)
    shared_dir = os.path.join(dir, '../test_field', user)
    if not os.path.exists(metadata):
        os.makedirs(metadata)
    if not os.path.exists(shared_dir):
        os.makedirs(shared_dir)
    return [metadata, shared_dir]

def check_file_database(metadata_dir):
    dir = metadata_dir + '/files.db'
    flag = os.path.exists(dir)
    conn = sqlite3.connect(dir)
    cursor = conn.cursor()
    if not flag:
        cursor.execute('''CREATE TABLE files
                            (dir text, md5 text, PRIMARY KEY(dir DESC))''')
        conn.commit()

    conn.close()



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')



    if len(sys.argv) > 2:
        user = sys.argv[1]
        #path = '/Users/xiangbinhu/GitHub/file-sharing-personal/watchdog_dev/' + "test_field/" +sys.argv[1] + '/'
        local_port = int(sys.argv[2])
        #remote_port = int(sys.argv[3])
        messenger_port = int(sys.argv[3])
    else:
        print "arg error"
        sys.exit()

    #PHASE 1 Check directories
    li_dir = check_directories(user)

    #PHASE 2 Load User data and databases
    check_file_database(li_dir[0])

    event_handler = P2PFSEventHandler(li_dir[0], li_dir[1], user)
    indicator = Indicator()
    connector = Connector(client.main, server.listener, local_port, messenger_port, indicator, li_dir[1], li_dir[0])

    coordinator = Coordinator(event_handler, connector, local_port)
    observer = Observer()
    observer.schedule(event_handler, li_dir[1], recursive=True)



    #PHASE 3 Start
    observer.start()
    coordinator.start()
    try:
        while True:
            #time.sleep(1)
            coordinator.tasklet()
    except KeyboardInterrupt:
        observer.stop()
        coordinator.terminate()
    observer.join()
    coordinator.join()
