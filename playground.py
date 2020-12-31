from flask import *
import os
import requests

base_path = os.getcwd()
#print(base_path)
# url = 'http://localhost:5000/images/products/1/'
url = 'http://localhost:5000/products/1/'

x = requests.get(url)
resp = json.loads(x.text)
print(resp)