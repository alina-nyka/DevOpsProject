# import  datetime
# from time import sleep
# print(datetime.datetime.now())
# sleep(3)
# print(datetime.datetime.now())

import requests

#response=requests.get("https://api.github.com")
#print(response.status_code) #console output: 200

def check_if_url_up(url):
    response = requests.get(url)
    if 200 <= response.status_code < 300:
        return True
    return False


print(check_if_url_up("https://github.com"))
