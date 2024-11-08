import requests, json


#Following code retrieves the token for a user.
#You can also use POSTMAN:Enter URL=http://127.0.0.1:8000/api-token-auth/ with method=POST,
# then select the 'Body' tab and under 'raw' enter {"username":"admin","password": "admin"} 
url = 'http://127.0.0.1:8000/api-token-auth/'
response = requests.post(url,data={'username': 'admin', 'password': 'admin'})
print('Response from server: ' + str(response.json()))
response_dict = json.loads(response.text)
print('token=',response_dict['token']) ## This token is valid infinitely long time.
print("#############################")


url = 'http://127.0.0.1:8000/hello/'
#NOTE I retrieved token from above and used it below.
#In postman: use URL=http://127.0.0.1:8000/hello/ with method=GET, then select 'Headers' tab and
#put key='Authorization' and value='Token 9a3faecbe7a754de5866d11eeeaf893f55aaa991'
headers = {'Authorization': 'Token 9a3faecbe7a754de5866d11eeeaf893f55aaa991'}
#or headers = {'Authorization': 'Token ' + response_dict['token']}
response = requests.get(url, headers=headers)
print('Response from server: ' + str(response.json()))

