# SIGOPS Distributed P2P File Sharing Project

## Table of Contents
  - [Requirements](#requirements)
  - [Server Side](#server_side)
  - [Sharing Client](#sharing_client)

## Requirements

* Python 3.6.3
* Redis 4.0.2
* Celery v4.1.0


## Server Side

**Updated by `Xgbn`**

This directory contains the server code for authentication. The server uses the Django Framework.

#### Implemented Features:

* Peer list is returned on successful login and signup
* Peers are divided into groups

#### TODO:

#### ISSUES:

* Need research on embedded authentication method of Django and MySQL database (__solved__)


#### Testing Procedures:
1. `cd testing/`... the tester only works in this directory
2. `chmod +x tester.sh`
3. `./tester.sh -s` to start the server
4. `./tester.sh -signup` to signup as a new user... __the URL field must have__ `http://` __in front__
5. `./tester.sh -login` to login as an old user

#### Asynchronous Tasks:
https://realpython.com/blog/python/asynchronous-tasks-with-django-and-celery/

lines:

```
redis-server
celery -A picha worker -l info
celery -A picha beat -l info
```


## Sharing Client

**Updated by `Atul-Nambudiri`**

This directory contains the file syncing code.

#### Implemented Features :
* Sync a whole directory
* Copy a directory when a new client comes up

#### How To :
* There are two python scripts, `server.py` and `client.py`. Server.py represents an existing client with fully synced files, while client.py is a newly spun up client.
* Put any files that you would like to sync in the in/ folder. You can have subfolders
* Run server.py
* In a separate terminal, run client.py
* The client will request all the files in servers synced folder. It will save the files into the out/ directory


#### Testing :

This directory is intended for testing purposes.

`connect.py` :      contains functions for interacting with the server

`tester.sh` :      see server_side readme for more information
