import requests

p={"page":2}
url="https://reqres.in/api/users" 
res = requests.post(url, params=p, data= open("load.json","r").read())
print(res)
print(res.json())
