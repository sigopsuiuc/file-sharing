#!/bin/bash

server_start(){
     python ../server_side/manage.py migrate
     python ../server_side/manage.py runserver
}

connect_to_server(){
    python ./connect.py $1
}


usage(){
     cat <<-EOF
Options:
     -s        get the server running
     -login    login as old user
     -signup   signup as new user
     ...
     other options waiting for implementation


EOF
}


if [ "$#" != "1" ]
then
     usage
elif [ "$1" == "-login" ]
then
    connect_to_server --login
elif [ "$1" == "-signup" ]
then
    connect_to_server --signup
elif [ "$1" == "-s" ]
then
    server_start
else
    usage
fi
