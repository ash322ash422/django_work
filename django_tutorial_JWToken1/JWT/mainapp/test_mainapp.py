import requests, json

#Following code retrieves the access and refresh token for a user.
url = 'http://127.0.0.1:8000/api/token/'
response = requests.post(url,data={'username': 'admin', 'password': 'admin'})
print('Response from server: ' + str(response.json()))
response_dict = json.loads(response.text)
print('access=',response_dict['access'])
print('refresh=',response_dict['refresh'])
print("#############################")

#Following sends the refresh token and gets a new access token.
url = 'http://127.0.0.1:8000/api/token/refresh/'
response = requests.post(url,
                         data={'username': 'admin',
                               'password': 'admin',
                               'refresh': response_dict['refresh'],
                               }, 
                         )
print('Response from server: ' + str(response.json()))
response_dict = json.loads(response.text)
print('access token=',response_dict['access'])
print("#############################")

#Now we try to access endpoints using these access token
url = 'http://127.0.0.1:8000/hello/'
headers = {'Authorization': 'Bearer ' + response_dict['access']}
response = requests.get(url, headers=headers)
print('Response from server: ' + str(response.json()))

