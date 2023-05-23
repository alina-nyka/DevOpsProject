import requests
from requests.exceptions import InvalidURL

try:
    response = requests.get("https:// ddfds")
except InvalidURL:
    print("invalid url was given")
