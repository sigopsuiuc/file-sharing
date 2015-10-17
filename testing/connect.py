import sys
import requests

URL = 'http://localhost:8000/peerlist/'

client = requests.session()

client.get(URL)
csrftoken = client.cookies['csrftoken']

data = {'username' : 'monkey', 'password' : '1234567', 'email' : 'foo@fool.com', 'csrfmiddlewaretoken':csrftoken}
r = client.post(URL, data=data, headers=dict(Referer=URL))

print r.status_code
print r.text



