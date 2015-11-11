import requests
import socket
import threading
import simplejson







UDP_IP = '127.0.0.1'
UDP_PORT = 5005
alive = True

def listen_on_port(port = UDP_PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((UDP_IP, port))

    while alive:

        data, addr = s.recvfrom(1024)
        print 'Connected to addr: ', addr
        #print 'received message: ', data
        try:
            parsed_data = simplejson.loads(data)
            print parsed_data
        except:
            print 'json parse error occured on message: "', data, '"'
            continue


    return




def main():
    proc1 = threading.Thread(target = listen_on_port)
    proc2 = threading.Thread(target = listen_on_port, args = (5004,))
    proc1.daemon = True
    proc2.daemon = True
    proc1.start()
    proc2.start()
    raw_input("Press Enter to Exist")




if __name__ == '__main__':
    main()
