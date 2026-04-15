import requests

url = "http://127.0.0.1:5000/prime_number/31"
response = requests.get(url).json()
print(response)