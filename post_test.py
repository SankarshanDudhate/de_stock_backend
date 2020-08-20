import requests

url = 'http://localhost:5000/products/'
myobj = {'category_id': 14}

x = requests.post(url, data = myobj)

print(x.text)