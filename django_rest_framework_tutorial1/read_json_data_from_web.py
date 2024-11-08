import requests

response = requests.get('http://127.0.0.1:8000/fruits')
print('response from server: ' + str(response.json()))