import requests
p={"page":2}
url="https://reqres.in/api/users" 
res = requests.get(url, params=p)
resp = res.json()
# print(resp['total'])
# print(resp['total_pages'])
# expected=resp['data'][1]['email']
assert resp['data'][1]['email']=="lindsay.ferguson@reqres.in","The email is wrong"
print("\n\ntest passed\n\n")