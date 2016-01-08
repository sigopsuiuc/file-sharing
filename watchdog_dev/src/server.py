import socket
import os
import re
import json
#sharing_directory = os.path.dirname(os.path.realpath(__file__)) + "/in/"

def get_file_list(sharing_directory):
    """
    Generates a list of directories and files in the shared folder
    """
    directories = []
    files = []
    for (dirpath, dirnames, filenames) in os.walk(sharing_directory):       #Recursively go through all the directories in the sharing directory
        dirpath = dirpath.replace(sharing_directory, "")        #Get the inner directory path within the sharing directory
        for directory in dirnames:
            if dirpath == "":
                directories.append("Directory:" + directory)        #Add the path to each directory within the sharing directory to the directories list
            else:
                directories.append("Directory:" + dirpath + "/" + directory)        #Add the path to each directory within the sharing directory to the directories list
        for file in filenames:
            if dirpath == "":
                files.append("File:" + file)        #Add the path to each file within the sharing directory to the files list
            else:
                files.append("File:" + dirpath + "/" + file)        #Add the path to each file within the sharing directory to the files list
    filelist = "\n".join(directories) + "\n" + "\n".join(files)
    return filelist


def setup_socket(port = 12345):
    """
    Sets up and returns a socket that will allow us to send files
    """
    s = socket.socket()             #Setup a socket connection on port 12345, which we will listen on
    host = '0.0.0.0'

    s.bind((host, port))
    s.listen(5)
    return s

def main(port = 12345, sharing_directory = '.'):
    """
    This will bind itself to a port and listen for any incoming connections
    """
    sock = setup_socket(port)
    while True:
        conn, addr = sock.accept()
        req = conn.recv(1024)
        if req == "Send Files":             #Send out the complete file list if a client requests it
            print("Sending out file_list")
            file_list = get_file_list()
            conn.send(file_list)
        elif "Request File" in req:         #Send out a file if a client requests it
             match_file = re.match("Request File:(.+)", req)
             file = match_file.group(1)
             print("Sending out: " + file)
             real_path = sharing_directory + file
             with open(real_path, "r") as file_content:
                resp = file_content.read(1024)
                while resp:
                    conn.send(resp)
                    resp = file_content.read(1024)
        conn.close()

def listener(port = 12345, sharing_directory = '.', indicatorQueue = None):
    """
    This will bind itself to a port and listen for any incoming connections
    """
    sock = setup_socket(port)
    while True:
        conn, addr = sock.accept()
        req = conn.recv(4096)
        if req == "Send Files":             #Send out the complete file list if a client requests it
            print("Sending out file_list")
            file_list = get_file_list(sharing_directory)
            conn.send(file_list)
        elif "Request File" in req:         #Send out a file if a client requests it
             match_file = re.match("Request File:(.+)", req)
             file = match_file.group(1)
             print("Sending out: " + file)
             real_path = sharing_directory + file
             with open(real_path, "r") as file_content:
                resp = file_content.read(1024)
                while resp:
                    conn.send(resp)
                    resp = file_content.read(1024)
        elif "event" in req:

            received = ""
            try:
                while (req):
                    received = received + req
                    req = conn.recv(4096)
                print received

                event_str = received[7:]
                event = json.loads(event_str)
                indicatorQueue.put(event)
            except socket.error:
                print "socket error in listener"


        conn.close()


if __name__ == "__main__":
    main()
