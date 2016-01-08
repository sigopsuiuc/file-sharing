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


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')



    if len(sys.argv) > 3:
        path = '/Users/xiangbinhu/GitHub/file-sharing-personal/watchdog_dev/' + "test_field/" +sys.argv[1] + '/'
        local_port = int(sys.argv[2])
        remote_port = int(sys.argv[3])
        messenger_port = int(sys.argv[4])
    else:
        print "arg error"
        sys.exit()

    peer_group_dict = Manager().dict()
    event_handler = P2PFSEventHandler()
    indicator = Indicator()
    connector = Connector(client.main, server.listener, remote_port, local_port, messenger_port, indicator, path, peer_group_dict)

    coordinator = Coordinator(event_handler, connector, remote_port, local_port, peer_group_dict)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
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
