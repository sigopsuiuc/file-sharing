#watchdog_dev

What is here?
----------------------------
In this directory we have our client codes and test directory for the clients

The code now only works when ip is 127.0.0.1

you need to have watchdog api installed

code does not work with python3



How to test?
----------------------------
##Step 1
start the server as is described in the README file in the root directory

##Step 2
make sure you have your client logged on to the server. remember what you filled
in in field __port__

##Step 3
go to watchdog_dev/src
python main.py <directory inside testfield> <listener_port> <messenger_port>
will start client program
e.g.
`python main.py 12 33221 33333` will let the watchdog check testfield/12
start a listener to send files to other client on 33221 and a listener on 33333 to
exchange messages or commands with the server and the other clients

the value of messenger_port should be the same as the value you filled in __port__ when you logged on

ISSUES
---------------------------
1. Client only respond if the other client has a newly created file or directory
2. Client will ask for all the files and directories once it knows other client has a
    newly created file __SOLVED__
3. The code now only works when ip is 127.0.0.1
