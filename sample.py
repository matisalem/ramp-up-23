import requests

request = requests.get('http://127.0.0.1:8001')

print(request.json)