import json
from http.cookies import SimpleCookie

rawdata = 'PUT_YOUR_DATA_HERE!!!'
cookie = SimpleCookie()
cookie.load(rawdata)
cookies = [{"name": k, "value": v.value} for k, v in cookie.items()]
cookie = json.dumps(cookies)
print(cookie)
with open('cookie.json', 'w') as f:
    f.write(cookie)