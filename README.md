# file-sharing

server_side
-----------------------------------------

#####updated by Xgbn

This directory contains the server code for authentication. The server uses Django Framework.

####implemented features:
* linked to a mysql database and uses a table named 'peer' for authentication testing
* able to receive requests and process requests
* have a admin page set up

####TODO:
* enable _POST_ request under the protection of csrf in polls/views.py	(__solved__)
* receive information from requests and store the information in the database for future reference
* set up authentication procedures.


###ISSUES:
* need research on embeded authentication method of Django and mysql database


testing
------------------------------------------
This directory is intended for testing purposes

connect.py will send post request to /polls/ and receive feedback from localhost

