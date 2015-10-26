import sys
import requests

URL = 'http://localhost:8000/peerlist/'

client = requests.session()

client.get(URL)
csrftoken = client.cookies['csrftoken']


#TODO

username = 'Xiangbin Hu'
password = 'I am poo'
email = 'hu.xgbn@gmail.com'
ngrok_domain = 'http://ngrokisgood.com'



data = {'username' : username, 'password' : password, 'email' : email, 'url' : ngrok_domain, 'csrfmiddlewaretoken':csrftoken}
r = client.post(URL, data=data, headers=dict(Referer=URL))

print r.status_code
print r.text
