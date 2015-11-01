import sys
import requests
import getpass
import sys
import argparse

#This is the URL
URL = 'http://localhost:8000/peerlist/'
URL_LOGIN = 'http://localhost:8000/peerlist/peerlogin/'


def new_user_signup():
    print 'this is the sign up session'
    try:
        client = requests.session()

        client.get(URL)
        csrftoken = client.cookies['csrftoken']
    except requests.exceptions.ConnectionError as e:
        print 'connection error... please check for configuration'
        sys.exit()


     #TODO

    username = raw_input('Please enter your username: ')
    password = getpass.getpass("Password for " + username + ": ")
    email = raw_input('Please enter the email: ')
    ngrok_domain = 'http://emptyfornow.com'



    data = {'username' : username, 'password' : password, 'email' : email, 'url' : ngrok_domain, 'csrfmiddlewaretoken':csrftoken}
    r = client.post(URL, data=data, headers=dict(Referer=URL))

    print 'Code: ' + str(r.status_code)
    print 'received message: \n' + r.text
    print '-----------------------'
    print 'End of sign up session'

def old_user_login():
    print 'this is the login session'
    try:
         client = requests.session()

         client.get(URL_LOGIN)
         csrftoken = client.cookies['csrftoken']
    except requests.exceptions.ConnectionError as e:
         print 'connection error... please check for configuration'
         sys.exit()

    username = raw_input('Please enter your username: ')
    password = getpass.getpass("Password for " + username + ": ")

    data = {'username' : username, 'password' : password, 'csrfmiddlewaretoken':csrftoken}
    r = client.post(URL_LOGIN, data=data, headers=dict(Referer=URL_LOGIN))

    print 'Code: ' + str(r.status_code)
    print 'received message \n' + r.text
    print '---------------------------------------'
    print 'End of login session'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--login", help="login as an old user", action="store_true")
    group.add_argument("--signup", help="sign up as a new user", action="store_true")
    args=parser.parse_args()
    if args.login:
        old_user_login()
    elif args.signup:
        new_user_signup()
    else:
        parser.print_help()
