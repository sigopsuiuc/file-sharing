import socket
import re
import os
import time

sharing_directory = os.path.dirname(os.path.realpath(__file__)) + "/out/"

def setup_socket(port = 12345):
	"""
	Sets up and returns a socket that will allow us to request files
	"""
	s = socket.socket()				#Setup a socket connection to port 12345, where the server will be listening
	host = socket.gethostbyname(socket.gethostname())
	#port = 12345
	print str(port)
	s.connect((host, port))
	return s

def request_file_list(port):
	"""
	Creates a socket to one of the other clients and requests the file list
	"""
	sock = setup_socket(port)
	print('Requesting File List')
	sock.send("Send Files")
	resp = sock.recv(1024)
	file_list = resp
	while resp:
		resp = sock.recv(1024)
		file_list += resp
	sock.close()
	return file_list

def request_file(file):
	"""
	Request the given file from another server and saves the file to disk
	"""
	real_path = sharing_directory + file
	with open(real_path, "w") as output:
		sock = setup_socket(port)
		print("Requesting file: " + file)
		sock.send("Request File:" + file)
		resp = sock.recv(1024)
		while(resp):
			output.write(resp)
			resp = sock.recv(1024)
		sock.close()

def create_directory(directory):
	"""
	Creates the specified directory within the shared folder
	"""
	print("Creating directory:" + sharing_directory + directory)
	real_path = sharing_directory + directory
	if not os.path.exists(real_path):
		os.makedirs(real_path)

def process_file_list(file_list):
	"""
	Parses the given file list. It goes through each item in the list. If the item is a directory,
	then that directory is made within the sharing folder. If its a file, then that file is requested from another client
	"""
	for line in file_list.split("\n"):
		match = re.match("Directory:(.+)", line)
		match_file = re.match("File:(.+)", line)
		if match != None:
			create_directory(match.group(1))
		elif match_file:
			request_file(match_file.group(1))

def main(dummy):
	"""
	This script acts as a newly spun up client. It will request the full file list from another existing client.
	This file list will include directories, and files. It will create all the directories that are needed,
	and then request the contents of all the files that are needed.
	"""
	while True:
		time.sleep(10)
		try:
			print "herere"
			file_list = request_file_list(dummy)
			process_file_list(file_list)
		except:
			print 'connection exception'
			continue

if __name__ == "__main__":
    main()
