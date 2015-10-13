import sys
import requests

URL = 'http://localhost:8000/polls/'

client = requests.session()

client.get(URL)
csrftoken = client.cookies['csrftoken']

data = {'fname' : 'cheers', 'csrfmiddlewaretoken':csrftoken}
r = client.post(URL, data=data, headers=dict(Referer=URL))

print r.status_code
print r.text



