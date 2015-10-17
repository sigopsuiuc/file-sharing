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
* send peer list to peer and receive list from peer

###ISSUES:
* need research on embeded authentication method of Django and mysql database


testing
------------------------------------------
This directory is intended for testing purposes

connect.py will send post request to /peerlist/ and receive feedback from localhost

