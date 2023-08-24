import requests

res = requests.get("https://reqres.in/api/users/2")
code= res.status_code
assert code==200, "Code dosen't match"
print("\n\n" ,res )
print("\n\n" ,res.text)
print("\n\n" ,res.content)
print("\n\n" ,res.json())