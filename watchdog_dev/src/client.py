import socket
import re
import os
import time
from multiprocessing import Queue
from Queue import Empty


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

def request_file_list_socket(remote_socket_tuple):
	"""
	Creates a socket to one of the other clients and requests the file list
	"""
	remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	remote_socket.connect(remote_socket_tuple)
	#not yet finished
	print('Requesting File List')
	remote_socket.send("Send Files")
	resp = remote_socket.recv(1024)
	file_list = resp
	while resp:
		resp = remote_socket.recv(1024)
		file_list += resp
	remote_socket.close()
	return file_list

def request_file(file, sharing_directory):
	"""
	Request the given file from another server and saves the file to disk
	"""
	real_path = sharing_directory + file
	with open(real_path, "w") as output:
		sock = setup_socket()
		print("Requesting file: " + file)
		sock.send("Request File:" + file)
		resp = sock.recv(1024)
		while(resp):
			output.write(resp)
			resp = sock.recv(1024)
		sock.close()

def request_file_socket(file, remote_socket_tuple, sharing_directory):
	"""
	Request the given file from another server and saves the file to disk
	"""

	real_path = sharing_directory + file
	with open(real_path, "w") as output:
		remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		remote_socket.connect(remote_socket_tuple)
		#sock = setup_socket()
		print("Requesting file: " + file)
		remote_socket.send("Request File:" + file)
		resp = remote_socket.recv(1024)
		while(resp):
			output.write(resp)
			resp = remote_socket.recv(1024)
		remote_socket.close()



def create_directory(directory, sharing_directory):
	"""
	Creates the specified directory within the shared folder
	"""
	print("Creating directory:" + sharing_directory + directory)
	real_path = sharing_directory + directory
	if not os.path.exists(real_path):
		os.makedirs(real_path)

def process_file_list(file_list, sharing_directory):
	"""
	Parses the given file list. It goes through each item in the list. If the item is a directory,
	then that directory is made within the sharing folder. If its a file, then that file is requested from another client
	"""
	for line in file_list.split("\n"):
		match = re.match("Directory:(.+)", line)
		match_file = re.match("File:(.+)", line)
		if match != None:
			create_directory(match.group(1), sharing_directory)
		elif match_file:
			request_file(match_file.group(1), sharing_directory)



def process_file_list_socket(file_list, remote_socket_tuple, sharing_directory):
	"""
	Parses the given file list. It goes through each item in the list. If the item is a directory,
	then that directory is made within the sharing folder. If its a file, then that file is requested from another client
	"""
	for line in file_list.split("\n"):
		match = re.match("Directory:(.+)", line)
		match_file = re.match("File:(.+)", line)
		if match != None:
			create_directory(match.group(1), sharing_directory)
		elif match_file:
			request_file_socket(match_file.group(1), remote_socket_tuple, sharing_directory)
def main(dummy, indicatorQueue, sharing_directory):
	"""

	"""

	print "entered client"
	while True:
		while True:
			try:
				print "start to fetch event"
				event = indicatorQueue.get()
				print "received indicator signal!"
				print event
				break
			except Empty:
				print "exception!"
		time.sleep(2)
		try:
			print "herere"
			remote_socket_tuple = (event[3], event[4])
			file_list = request_file_list_socket(remote_socket_tuple)
			process_file_list_socket(file_list, remote_socket_tuple, sharing_directory)
		except socket.error as msg:
			print 'connection exception: ' + msg
			continue

if __name__ == "__main__":
    main()
