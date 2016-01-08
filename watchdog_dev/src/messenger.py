import socket
import logging
import re
import json
class Messenger:

    def __init__(self, port, peer_group_dict):
        self.port = port
        self.group = peer_group_dict
        self.msg_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.msg_socket.bind(('0.0.0.0', port))
        self.logger = logging.getLogger('messenger_report')

    def process(self, indicator_queue):
        self.msg_socket.listen(5)
        while True:
            conn, addr = self.msg_socket.accept()
            #data, addr = self.msg_socket.recvfrom(4096)
            data = conn.recv(4096)
            received = ""
            while(data):
                received = received + data
                data = conn.recv(4096)
            #received = received + data
            self.logger.debug('from: %s', str(addr))
            self.logger.debug('received data is: %s', received)
            s = re.search('\{.*?\}', received)
            e = re.match('event\:.*', received)
            if s:
                extracted = s.group(0)
                self.logger.debug('extracted data is: %s', extracted)
                parsed = json.loads(extracted)
                self.group.update(parsed)

            else:
                self.logger.debug('none json object found')

            if e:
                self.logger.debug('%s', received)
                event = re.search('\[.*?\]', received)
                event_obj = json.loads(event.group(0))
                indicator_queue.put(event_obj)
            self.logger.debug('now the group members we have on record is: %s', self.group)

            #print received

            conn.close()
