import sys
import time
import logging
#import multiprocessing
from watchdog.observers import Observer
#from watchdog.events import LoggingEventHandler
from eventhandler import P2PFSEventHandler
from tasks import Coordinator, Connector
import client
import server


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = P2PFSEventHandler()
    coordinator = Coordinator(event_handler)
    connector = Connector(client.main, server.listener, 12345, 12345)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    connector.start()
    try:
        while True:
            #time.sleep(1)
            coordinator.tasklet()
    except KeyboardInterrupt:
        observer.stop()
        connector.terminate()
    observer.join()
    connector.join()
