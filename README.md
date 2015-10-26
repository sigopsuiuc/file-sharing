# file-sharing

server_side
-----------------------------------------

#####updated by Xgbn

This directory contains the server code for authentication. The server uses Django Framework.

####implemented features:
* able to receive requests and process requests
* have an admin page set up

####TODO:
* enable _POST_ request under the protection of csrf in polls/views.py	(__solved__)
* <s>receive information from requests and store the information in the database for future reference</s>
* set up authentication procedures.
* send peer list to peer and receive list from peer(__solved__)
###ISSUES:
* need research on embeded authentication method of Django and mysql database(__solved__)


####Testing procedures
1. file-sharing/testing/connect.py contains the necessary information to send a valid request to the server
2. `python connect.py` will send the request and receive the response containing the dictionary of peers

sharing_client
-----------------------------------------

#####updated by Atul-Nambudiri

This directory contains the file syncing code

####implemented features:
* Sync a whole directory
* Copy a directory when a new client comes up

###HowTo:
* There are two python scripts, server.py and client.py. Server.py represents an existing client with fully synced files, while client.py is a newly spun up client.
* Put any files that you would like to sync in the in/ folder. You can have subfolders
* Run server.py
* In a seperate terminal, run client.py
* The client will request all the files in servers synced folder. It will save the files into the out/ directory


testing
------------------------------------------
This directory is intended for testing purposes

connect.py will send post request to /peerlist/ and receive feedback from localhost
